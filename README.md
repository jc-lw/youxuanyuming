项目搬运，这两位大佬 [tianshipapa](https://github.com/tianshipapa) 和 [ymyuuu](https://github.com/ymyuuu/BestDomain)
只是合并项目
# cfipcaiji
每3小时自动抓取 https://monitor.gacjie.cn/page/cloudflare/ipv4.html和 https://ip.164746.xyz 的优选ip，
形成ip.txt 还有js自动生成的https://cf.090227.xyz 和 https://stock.hostmonit.com/CloudFlareYes
- caijiip.yml文件夹里面改成你自己的
![image](https://github.com/user-attachments/assets/723cd14e-d108-4f2d-9780-710410a1b955)


# BestDomain

## 使用说明

1. 创建 Cloudflare API 令牌
   - 访问 [Cloudflare API Tokens](https://dash.cloudflare.com/profile/api-tokens)
   - 选择需要解析的域名，创建编辑 DNS 权限的 `CF_API_TOKEN`

<img width="1440" alt="image" src="https://github.com/user-attachments/assets/a2000336-9e85-41c8-85f5-30ec75362605">

2. 设置 GitHub Secrets
   - 在你的 GitHub 仓库中，设置 `CF_API_TOKEN` 为你的 Cloudflare API 令牌
   - 参考 GitHub 文档：[Creating and storing encrypted secrets](https://docs.github.com/zh/actions/security-guides/using-secrets-in-github-actions)

3. 配置 GitHub Actions 定时任务
   - 编辑 [.github/workflows/main.yml](.github/workflows/main.yml) 文件，设置 `cron` 表达式以定义任务运行时间
"# youxuanyuming" 
"# youxuanyuming" 
