import re
import pandas as pd
import matplotlib.pyplot as plt
import os

# --------------------------
# Configuration
# --------------------------

schemes = ['cubic', 'bbr', 'copa']
profile = '50Mb-10ms'
base_dir = '/home/ramya/pantheon_logs'

# --------------------------
# Helper Functions
# --------------------------

def parse_datalink(fn):
    df = pd.read_csv(fn, sep=r"\s+", header=None, usecols=[0, 3], names=['t', 'bytes'])
    df['bytes'] = pd.to_numeric(df['bytes'], errors='coerce')
    df.dropna(inplace=True)
    df['bits'] = df['bytes'] * 8
    return df

def parse_acklink(fn, interval=0.1):
    times = []
    with open(fn) as f:
        for line in f:
            if 'dropped' in line:
                ts = float(line.split()[0])
                times.append(ts)

    # Convert to datetime
    time_index = pd.to_datetime(times, unit='s')
    
    # Build Series with datetime index
    s = pd.Series(1, index=pd.DatetimeIndex(time_index, name='t'))

    # Now resample correctly
    loss = s.resample(f'{int(interval * 1000)}ms').sum().fillna(0)
    return loss


# --------------------------
# Plot Throughput
# --------------------------

plt.figure()
for cc in schemes:
    file_path = os.path.join(base_dir, f"{cc}_mm_datalink_run1.log")
    df = parse_datalink(file_path)
    plt.plot(df.t, df.bits / 1e6, label=cc)
plt.xlabel('Time (s)')
plt.ylabel('Throughput (Mbps)')
plt.title(f'Throughput - {profile}')
plt.legend()
plt.savefig('throughput_profile1.png', bbox_inches='tight')
plt.close()

# --------------------------
# Plot Packet Loss
# --------------------------

plt.figure()
for cc in schemes:
    file_path = os.path.join(base_dir, f"{cc}_mm_acklink_run1.log")
    loss = parse_acklink(file_path)
    plt.plot(loss.index, loss.values, label=cc)
plt.xlabel('Time (s)')
plt.ylabel('Loss count per interval')
plt.title(f'Loss - {profile}')
plt.legend()
plt.savefig('loss_profile1.png', bbox_inches='tight')
plt.close()

# --------------------------
# RTT and Throughput Summary
# --------------------------

rtt_data = []


for cc in schemes:
    stats_file = os.path.join(base_dir, f"{cc}_stats_run1.log")
    with open(stats_file) as f:
        content = f.read()

        # Debug check if expected pattern is found
        match_avg = re.search(r'avg rtt:\s*([\d\.]+)', content)
        match_p95 = re.search(r'95th rtt:\s*([\d\.]+)', content)

        if not match_avg or not match_p95:
            print(f"[ERROR] Could not find RTT values in {stats_file}")
            print("[DEBUG] File content:")
            print(content)
            continue  # Skip this scheme if we can't parse it

        avg = float(match_avg.group(1))
        p95 = float(match_p95.group(1))
        datalink_file = os.path.join(base_dir, f"{cc}_mm_datalink_run1.log")
        thp = parse_datalink(datalink_file)['bits'].mean() / 1e6
        rtt_data.append((cc, profile, avg, p95, thp))


df_rtt = pd.DataFrame(rtt_data, columns=['protocol', 'profile', 'avg_rtt', '95_rtt', 'avg_throughput'])

# --------------------------
# Scatter Plot: RTT vs Throughput
# --------------------------

plt.figure()
for _, row in df_rtt.iterrows():
    plt.scatter(row.avg_rtt, row.avg_throughput)
    plt.text(row.avg_rtt, row.avg_throughput, row.protocol)
plt.xlabel('Avg RTT (ms)')
plt.ylabel('Avg Throughput (Mbps)')
plt.title('Performance Scatter')
plt.savefig('perf_scatter.png', bbox_inches='tight')
plt.close()

# --------------------------
# Print Summary Table
# --------------------------

print("\n--- RTT & Throughput Summary ---")
print(df_rtt.to_string(index=False))

