import os
import json
from huggingface_hub import HfApi, HfFolder, RepositoryNotFoundError

# 用于存储用户信息的文件名
USER_INFO_FILE = "user_info.json"

def save_user_info(username, token):
    """保存用户信息到本地文件"""
    user_data = {"username": username, "token": token}
    with open(USER_INFO_FILE, "w") as f:
        json.dump(user_data, f)
    print(f"用户信息已保存，用户名：{username}")

def load_user_info():
    """从本地文件加载用户信息"""
    if os.path.exists(USER_INFO_FILE):
        with open(USER_INFO_FILE, "r") as f:
            user_data = json.load(f)
        print(f"加载用户信息，用户名：{user_data['username']}")
        return user_data['username'], user_data['token']
    else:
        print("没有找到用户信息文件。")
        return None, None

def upload_file_to_dataset(file_path, dataset_repo_id, token):
    """上传文件到指定的Hugging Face数据集"""
    api = HfApi()
    try:
        api.upload_file(
            path_or_fileobj=file_path,
            path_in_repo=file_path.split("/")[-1],  # 将文件名作为路径存储在数据集中
            repo_id=dataset_repo_id,
            repo_type="dataset",
            token=token
        )
        print(f"文件 {file_path} 已成功上传到数据集 {dataset_repo_id}。")
    except RepositoryNotFoundError:
        print(f"数据集 {dataset_repo_id} 未找到。请检查数据集ID和用户的访问权限。")
    except Exception as e:
        print(f"文件上传失败: {str(e)}")

def main():
    """主函数，用于处理用户输入和文件上传"""
    username, token = load_user_info()

    if not token:
        # 如果没有找到用户信息，则请求用户输入
        username = input("请输入您的Hugging Face用户名: ")
        token = input("请输入您的Hugging Face访问令牌: ")
        save_user_info(username, token)
    
    file_path = input("请输入要上传的文件路径: ")
    dataset_repo_id = input("请输入目标数据集ID (例如: username/dataset_name): ")
    
    upload_file_to_dataset(file_path, dataset_repo_id, token)

if __name__ == "__main__":
    main()
