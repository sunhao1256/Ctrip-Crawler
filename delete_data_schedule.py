import os
import shutil
import schedule
import time

# 定义需要删除的目录列表
directories_to_clean = [
    "/Users/zero/Projects/Personal/Ctrip-Crawler/2025-02-01",
    "/Users/zero/Projects/Personal/Ctrip-Crawler/2025-02-02",
    "/Users/zero/Projects/Personal/Ctrip-Crawler/2025-02-03",
]

def delete_directories(directories):
    for directory in directories:
        try:
            if os.path.exists(directory):
                shutil.rmtree(directory)  # 删除目录及其所有内容
                print(f"成功删除目录及内容: {directory}")
            else:
                print(f"目录不存在: {directory}")
        except Exception as e:
            print(f"删除目录时出错: {directory}, 错误信息: {e}")

# 定时任务：每隔 10 分钟运行
def job():
    print(f"任务开始: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    delete_directories(directories_to_clean)
    print(f"任务完成: {time.strftime('%Y-%m-%d %H:%M:%S')}")

schedule.every(10).minutes.do(job)

# 持续运行定时任务
if __name__ == "__main__":
    print("定时任务启动...")
    while True:
        schedule.run_pending()
        time.sleep(1)