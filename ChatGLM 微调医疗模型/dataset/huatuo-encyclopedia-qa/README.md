---
license: apache-2.0
task_categories:
- text-generation
language:
- zh
tags:
- medical
size_categories:
- 100K<n<1M
---
# Dataset Card for Huatuo_encyclopedia_qa



## Dataset Description

- **Homepage: https://www.huatuogpt.cn/** 
- **Repository: https://github.com/FreedomIntelligence/HuatuoGPT** 
- **Paper: https://arxiv.org/abs/2305.01526** 
- **Leaderboard:** 
- **Point of Contact:** 



### Dataset Summary

This dataset has a total of 364,420 pieces of medical QA data, some of which have multiple questions in different ways. We extract medical QA pairs from plain texts (e.g., medical encyclopedias and medical articles). We collected 8,699 encyclopedia entries for diseases and 2,736 encyclopedia entries for medicines on Chinese Wikipedia. Moreover, we crawled 226,432 high-quality medical articles from the Qianwen Health website.




## Dataset Creation



### Source Data

https://zh.wikipedia.org/wiki/  

https://51zyzy.com/




## Citation

```
@misc{li2023huatuo26m,
      title={Huatuo-26M, a Large-scale Chinese Medical QA Dataset}, 
      author={Jianquan Li and Xidong Wang and Xiangbo Wu and Zhiyi Zhang and Xiaolong Xu and Jie Fu and Prayag Tiwari and Xiang Wan and Benyou Wang},
      year={2023},
      eprint={2305.01526},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
