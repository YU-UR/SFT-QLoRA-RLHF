# ChatGLM 医疗领域模型微调与部署

基于医疗领域公开数据集，使用 **LLaMA-Factory + LoRA/QLoRA** 对 `GLM-4-9B-Chat` 进行监督微调（SFT），完成医疗问答模型训练、LoRA 权重合并，并使用 **vLLM** 部署为 OpenAI 兼容 API 服务。

> 预计运行时间：2–4 小时  
> 推荐 GPU：24GB 显存的 NVIDIA RTX 3090 / RTX 4090

---

## 1. 项目目标

本项目主要完成以下内容：

- 了解医疗领域公开数据集及评测 Benchmark
- 完成医疗问答数据的获取、整理和格式转换
- 掌握 Alpaca 格式数据集的构造方法
- 使用 [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) 完成模型 SFT
- 使用 LoRA / QLoRA 进行参数高效微调
- 理解量化、LoRA、SFT、验证集等训练配置
- 合并 LoRA Adapter 与 Base Model
- 使用 [vLLM](https://github.com/vllm-project/vllm) 部署微调后的模型
- 通过 OpenAI 兼容 API 调用部署后的医疗问答模型

---

# 2. 项目流程

整体流程如下：

```text
医疗公开数据集
      │
      ▼
Huatuo-26M
      │
      ▼
数据清洗与格式转换
      │
      ▼
Alpaca 数据格式
      │
      ▼
LLaMA-Factory 数据集配置
      │
      ▼
GLM-4-9B-Chat
      │
      ▼
LoRA / QLoRA + SFT
      │
      ▼
LoRA Checkpoint
      │
      ▼
LoRA + Base Model 合并
      │
      ▼
Merge Model
      │
      ▼
vLLM
      │
      ▼
OpenAI Compatible API
      │
      ▼
医疗问答服务
