# LLM Fine-Tuning & Alignment Projects

**大语言模型微调与对齐实践项目集**

本仓库整理了大语言模型（LLM）微调、参数高效微调（PEFT）、QLoRA、Flash Attention、SFT 以及 RLHF 等相关实践项目，涵盖从数据处理、模型微调到模型对齐的完整实验流程。

This repository contains a collection of practical projects covering Large Language Model (LLM) fine-tuning, Parameter-Efficient Fine-Tuning (PEFT), QLoRA, Flash Attention, Supervised Fine-Tuning (SFT), and Reinforcement Learning from Human Feedback (RLHF). The projects cover the workflow from data preparation and model fine-tuning to model alignment.

---

## 📚 Projects / 项目列表

### 1. [ChatGLM 微调医疗模型 / ChatGLM Medical Model Fine-Tuning](https://github.com/YU-UR/SFT-QLoRA-RLHF/tree/main/ChatGLM%20%E5%BE%AE%E8%B0%83%E5%8C%BB%E7%96%97%E6%A8%A1%E5%9E%8B)

**项目方向 / Topic:**
医疗领域大语言模型微调 / Medical Domain LLM Fine-Tuning

**技术栈 / Technologies:**

* ChatGLM / GLM4-Chat
* LLaMA-Factory
* LoRA / QLoRA
* Alpaca Dataset Format
* Hugging Face Transformers

#### 🇨🇳 中文简介

本项目基于 [FreedomIntelligence/Huatuo-26M](https://github.com/FreedomIntelligence/Huatuo-26M) 华佗数据集中的 `huatuo_encyclopedia_qa` 百科问答数据，构建医疗百科问答模型。

主要流程包括：

1. 获取并处理华佗医疗百科问答数据集；
2. 将原始数据转换为 **Alpaca 格式**；
3. 使用 **LLaMA-Factory** 构建模型微调流程；
4. 基于 **GLM4-Chat** 进行 LoRA / QLoRA 参数高效微调；
5. 保存 LoRA / QLoRA Adapter 参数；
6. 使用 LLaMA-Factory 提供的 Merge 功能，将 LoRA 参数与 Base Model 参数进行合并；
7. 获得可用于后续部署和推理的完整模型。

LoRA / QLoRA 微调过程中保存的 Checkpoint 主要包含 Adapter 参数，而不是完整的 Base Model。因此，在实际部署时，需要将 Adapter 参数与原始 Base Model 进行 Merge。

对应的模型合并配置文件：

`llama_factory_configs/glm4_lora_merge.yaml`

#### 🇬🇧 English Description

This project fine-tunes a medical question-answering model using the `huatuo_encyclopedia_qa` dataset from the [Huatuo-26M](https://github.com/FreedomIntelligence/Huatuo-26M) medical dataset.

The main workflow includes:

1. Preparing and preprocessing the Huatuo medical QA dataset;
2. Converting the dataset into **Alpaca format**;
3. Building the fine-tuning pipeline with **LLaMA-Factory**;
4. Performing parameter-efficient fine-tuning on **GLM4-Chat** using LoRA / QLoRA;
5. Saving LoRA / QLoRA adapter checkpoints;
6. Merging the LoRA adapter parameters with the Base Model using LLaMA-Factory;
7. Producing a complete model for subsequent deployment and inference.

The checkpoints generated during LoRA / QLoRA fine-tuning mainly contain adapter parameters rather than the complete Base Model. Therefore, the adapter parameters need to be merged with the original Base Model before deployment.

**Merge configuration:**

`llama_factory_configs/glm4_lora_merge.yaml`

---

### 2. [QLoRA Fine-Tune LLaMA / QLoRA 微调 LLaMA](https://github.com/YU-UR/SFT-QLoRA-RLHF/tree/main/QLoRA%20finetune%20LLaMa)

**项目方向 / Topic:**
基于 QLoRA 的大语言模型参数高效微调 / Parameter-Efficient LLM Fine-Tuning with QLoRA

**技术栈 / Technologies:**

* LLaMA
* QLoRA
* LoRA
* 4-bit Quantization
* Hugging Face Transformers
* PEFT

#### 🇨🇳 中文简介

本项目实践 **QLoRA（Quantized Low-Rank Adaptation）** 技术，通过低比特量化与 LoRA 相结合，在降低显存占用的同时完成大语言模型的参数高效微调。

项目重点包括：

* LLaMA 模型加载；
* 4-bit 量化；
* LoRA Adapter 配置；
* QLoRA 微调流程；
* Training Configuration 配置；
* Checkpoint 保存；
* 微调后模型推理。

#### 🇬🇧 English Description

This project demonstrates **QLoRA (Quantized Low-Rank Adaptation)** for parameter-efficient fine-tuning of LLaMA models.

QLoRA combines low-bit quantization with LoRA adapters to significantly reduce GPU memory consumption while enabling efficient fine-tuning of large language models.

Key topics include:

* Loading LLaMA models;
* 4-bit quantization;
* LoRA adapter configuration;
* QLoRA fine-tuning;
* Training configuration;
* Checkpoint management;
* Inference with the fine-tuned model.

**Project Documentation / 项目文档：**

[QLoRA Fine-Tune LLaMA 项目手册](https://github.com/YU-UR/SFT-QLoRA-RLHF/blob/main/QLoRA%20finetune%20LLaMa/%E9%A1%B9%E7%9B%AE%E6%89%8B%E5%86%8C%EF%BC%9AQLoRA%20finetune%20LLaMa.pdf)

---

### 3. [QLoRA + Flash Attention](https://github.com/YU-UR/SFT-QLoRA-RLHF/tree/main/QLoRA%2BFlash%20Attention)

**项目方向 / Topic:**
QLoRA 与高效 Attention 机制结合 / Efficient LLM Fine-Tuning with QLoRA and Flash Attention

**技术栈 / Technologies:**

* QLoRA
* LoRA
* Flash Attention
* Transformer
* Hugging Face Transformers

#### 🇨🇳 中文简介

本项目在 QLoRA 参数高效微调的基础上，引入 **Flash Attention**，探索显存优化和 Attention 计算效率提升。

项目主要关注：

* QLoRA 参数高效微调；
* Flash Attention 原理与应用；
* Transformer Attention 计算优化；
* 显存占用优化；
* 大模型训练效率优化。

#### 🇬🇧 English Description

This project combines **QLoRA** with **Flash Attention** to explore more memory-efficient and computationally efficient LLM fine-tuning.

The project focuses on:

* Parameter-efficient fine-tuning with QLoRA;
* Flash Attention;
* Transformer attention optimization;
* GPU memory optimization;
* Improving training efficiency for large language models.

**Project Documentation / 项目文档：**

[QLoRA + Flash Attention 项目手册](https://github.com/YU-UR/SFT-QLoRA-RLHF/blob/main/QLoRA%2BFlash%20Attention/%E9%A1%B9%E7%9B%AE%E6%89%8B%E5%86%8C-QLoRA%20FlashAttention.pdf)

---

### 4. [RLHF 推荐模型对齐 / RLHF Recommendation Model Alignment](https://github.com/YU-UR/SFT-QLoRA-RLHF/tree/main/RLHF%E6%8E%A8%E8%8D%90%E6%A8%A1%E5%9E%8B%E5%AF%B9%E9%BD%90)

**项目方向 / Topic:**
基于 RLHF 的推荐模型对齐 / Recommendation Model Alignment with RLHF

**技术栈 / Technologies:**

* RLHF
* Reward Modeling
* Human Preference Alignment
* LLM Alignment

#### 🇨🇳 中文简介

本项目围绕 **RLHF（Reinforcement Learning from Human Feedback）** 展开模型对齐实践，探索如何利用人类偏好反馈优化模型输出，使模型生成结果更加符合目标任务和用户偏好。

项目重点包括：

* 人类偏好数据；
* Reward Model；
* 模型输出评价；
* 强化学习优化；
* RLHF 对齐流程。

#### 🇬🇧 English Description

This project explores **Reinforcement Learning from Human Feedback (RLHF)** for recommendation model alignment.

The goal is to investigate how human preference feedback can be incorporated into the training process to optimize model behavior and make generated outputs better aligned with task requirements and user preferences.

Key topics include:

* Human preference data;
* Reward modeling;
* Output evaluation;
* Reinforcement learning optimization;
* RLHF-based model alignment.

**Project Documentation / 项目文档：**

[RLHF 推荐模型对齐项目手册](https://github.com/YU-UR/SFT-QLoRA-RLHF/blob/main/RLHF%E6%8E%A8%E8%8D%90%E6%A8%A1%E5%9E%8B%E5%AF%B9%E9%BD%90/%E9%A1%B9%E7%9B%AE%E6%89%8B%E5%86%8C-RLHF%E6%8E%A8%E8%8D%90%E6%A8%A1%E5%9E%8B%E5%AF%B9%E9%BD%90.pdf)

---

### 5. [SFT 推荐模型微调 / SFT Recommendation Model Fine-Tuning](https://github.com/YU-UR/SFT-QLoRA-RLHF/tree/main/SFT%E6%8E%A8%E8%8D%90%E6%A8%A1%E5%9E%8B%E5%BE%AE%E8%B0%83)

**项目方向 / Topic:**
基于 SFT 的推荐模型微调 / Supervised Fine-Tuning for Recommendation Models

**技术栈 / Technologies:**

* SFT
* Supervised Fine-Tuning
* LLM Fine-Tuning
* Transformer
* Hugging Face

#### 🇨🇳 中文简介

本项目实践 **SFT（Supervised Fine-Tuning，监督微调）**，通过构建高质量的指令-回答训练数据，使预训练语言模型学习特定任务的数据分布和输出模式。

项目主要包括：

* 指令数据构建；
* 数据预处理；
* SFT 训练；
* 模型参数配置；
* Checkpoint 保存；
* 微调模型推理与效果验证。

#### 🇬🇧 English Description

This project demonstrates **Supervised Fine-Tuning (SFT)** for recommendation models.

The project uses instruction-response training data to adapt a pretrained language model to a specific task and desired output format.

Key topics include:

* Instruction dataset construction;
* Data preprocessing;
* Supervised fine-tuning;
* Training configuration;
* Checkpoint management;
* Inference and evaluation of the fine-tuned model.

**Project Documentation / 项目文档：**

[SFT 推荐模型微调项目手册](https://github.com/YU-UR/SFT-QLoRA-RLHF/blob/main/SFT%E6%8E%A8%E8%8D%90%E6%A8%A1%E5%9E%8B%E5%BE%AE%E8%B0%83/%E9%A1%B9%E7%9B%AE%E6%89%8B%E5%86%8C%EF%BC%9ASFT%E6%8E%A8%E8%8D%90%E6%A8%A1%E5%9E%8B%E5%BE%AE%E8%B0%83.pdf)

---

## 🧩 Technical Overview / 技术体系

| 技术方向            | 中文          | English                                    |
| --------------- | ----------- | ------------------------------------------ |
| SFT             | 监督微调        | Supervised Fine-Tuning                     |
| LoRA            | 低秩适配        | Low-Rank Adaptation                        |
| QLoRA           | 量化低秩适配      | Quantized Low-Rank Adaptation              |
| PEFT            | 参数高效微调      | Parameter-Efficient Fine-Tuning            |
| Flash Attention | 高效注意力机制     | Efficient Attention                        |
| RLHF            | 基于人类反馈的强化学习 | Reinforcement Learning from Human Feedback |
| LLaMA-Factory   | 大模型微调框架     | LLM Fine-Tuning Framework                  |
| Alpaca Format   | 指令数据格式      | Instruction Dataset Format                 |

---

## 🔄 Overall Workflow / 整体流程

```text
                    LLM Fine-Tuning & Alignment
                              │
             ┌────────────────┴────────────────┐
             │                                 │
       Data Preparation                   Model Training
       数据准备                              模型训练
             │                                 │
     Dataset Processing              ┌─────────┴─────────┐
     数据清洗/转换                    │                   │
             │                      SFT                PEFT
      Alpaca Format                 │             LoRA / QLoRA
      指令数据格式                   │                   │
             │                      └─────────┬─────────┘
             │                                │
             │                         Flash Attention
             │                                │
             └────────────────┬───────────────┘
                              │
                         Model Alignment
                            模型对齐
                              │
                            RLHF
                              │
                    Reward / Human Feedback
                              │
                              ▼
                    Fine-tuned / Aligned LLM
```

---

## 🎯 Learning Objectives / 学习目标

### 中文

通过这些项目，系统学习大语言模型从**数据准备 → 监督微调 → 参数高效微调 → 训练优化 → 模型合并 → 模型对齐**的完整流程。

重点掌握：

* 大模型训练数据处理；
* Alpaca 指令数据格式；
* SFT 监督微调；
* LoRA / QLoRA 参数高效微调；
* 低比特量化；
* Flash Attention；
* Checkpoint 与 Adapter 管理；
* LoRA 与 Base Model Merge；
* RLHF 模型对齐；
* 微调模型推理与部署。

### English

These projects provide a practical learning path covering the complete LLM workflow:

**Data Preparation → SFT → PEFT → Training Optimization → Model Merging → Model Alignment**

The main learning objectives include:

* LLM training data preprocessing;
* Alpaca instruction format;
* Supervised Fine-Tuning;
* LoRA / QLoRA parameter-efficient fine-tuning;
* Low-bit quantization;
* Flash Attention;
* Checkpoint and adapter management;
* LoRA and Base Model merging;
* RLHF-based model alignment;
* Inference and deployment of fine-tuned models.

---

## 🛠️ Main Tools & Frameworks / 主要工具与框架

* **LLaMA-Factory**
* **Hugging Face Transformers**
* **PEFT**
* **PyTorch**
* **LoRA / QLoRA**
* **Flash Attention**
* **RLHF**
* **ChatGLM / GLM4**
* **LLaMA**
* **Huatuo-26M**

---

## 📌 Repository Structure / 仓库结构

```text
SFT-QLoRA-RLHF/
│
├── ChatGLM 微调医疗模型/
│   ├── data/
│   ├── llama_factory_configs/
│   └── ...
│
├── QLoRA finetune LLaMa/
│   ├── 项目代码
│   └── 项目手册
│
├── QLoRA+Flash Attention/
│   ├── 项目代码
│   └── 项目手册
│
├── RLHF推荐模型对齐/
│   ├── 项目代码
│   └── 项目手册
│
└── SFT推荐模型微调/
    ├── 项目代码
    └── 项目手册
```

---

## 📖 References / 参考资料

* [Huatuo-26M](https://github.com/FreedomIntelligence/Huatuo-26M)
* [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)
* [Hugging Face Transformers](https://github.com/huggingface/transformers)
* [Hugging Face PEFT](https://github.com/huggingface/peft)

---

## 👤 Author

**YU-UR**

GitHub: https://github.com/YU-UR
