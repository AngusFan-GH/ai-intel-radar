# AI 情报雷达日报（2026-11-26）

当前展示池累计 240 条事件。日报已改成按厂商合并展示，并补充“摘要 / 推荐理由 / 关键信号”，帮助快速判断什么值得继续点开。

数据概况： 厂商新品 4 条； 新模型 121 条； 新开源项目 100 条； 其他观察 15 条。

## 厂商新品（4）

### Together AI（2 条重点）

- [Introducing preemptible compute: the same compute, half the price](https://www.together.ai/blog/introducing-preemptible-compute-the-same-compute-half-the-price)
  - 中文说明：主体：Together AI；事件类型：产品发布；来源：官方资讯源；评分：62.04；标签：未打标签。
  - 摘要：这是官方发布源中的一条更新，核心内容是：Together GPU Clusters now supports preemptible compute: the same GPU capacity at a flat 50% of the on-demand rate, with…
  - 推荐理由：来自官方发布面，可信度比二手转述更高
  - 关键信号：信号来源：官方 RSS。
  - 原文摘要：Together GPU Clusters now supports preemptible compute: the same GPU capacity at a flat 50% of the on-demand rate, with a five-minute drain window.

- [Introducing Together Storage Accelerator: fast, free data caching for your GPU cluster](https://www.together.ai/blog/introducing-together-storage-accelerator)
  - 中文说明：主体：Together AI；事件类型：产品发布；来源：官方资讯源；评分：51.00；标签：未打标签。
  - 摘要：这是官方发布源中的一条更新，核心内容是：Together Storage Accelerator is a distributed caching layer for Together GPU Clusters: about 20x faster warm reads, one…
  - 推荐理由：来自官方发布面，可信度比二手转述更高
  - 关键信号：信号来源：官方 RSS。
  - 原文摘要：Together Storage Accelerator is a distributed caching layer for Together GPU Clusters: about 20x faster warm reads, one origin fetch per cluster, no application changes, and it's…

### OpenAI（1 条重点）

- [Richpanel helps companies automate 50% of support in 30 days](https://openai.com/business/customer-stories/richpanel-ai-customer-support)
  - 中文说明：主体：OpenAI；事件类型：产品发布；来源：官方资讯源；评分：59.38；标签：Agent。
  - 摘要：这是官方发布源中的一条更新，核心内容是：Richpanel uses GPT-6 Astra and GPT-6.1 Sol to equip its AI support agents with tools and procedures, and GPT-6 Luna for…
  - 推荐理由：来自官方发布面，可信度比二手转述更高
  - 关键信号：信号来源：官方 RSS。
  - 原文摘要：Richpanel uses GPT-6 Astra and GPT-6.1 Sol to equip its AI support agents with tools and procedures, and GPT-6 Luna for their conversations.

### Qwen（1 条重点）

- [Qwen3 TTS is now available on Together AI](https://www.together.ai/blog/qwen3-tts)
  - 中文说明：主体：Qwen；事件类型：产品发布；来源：官方资讯源；评分：51.00；标签：语音。
  - 摘要：这是官方发布源中的一条更新，核心内容是：Qwen3 TTS is now available on Together AI. Keep one voice across your product, change its tone with a plain-language in…
  - 推荐理由：来自官方发布面，可信度比二手转述更高
  - 关键信号：信号来源：官方 RSS。
  - 原文摘要：Qwen3 TTS is now available on Together AI. Keep one voice across your product, change its tone with a plain-language instruction and move it between 10 languages, with first audio…

## 新模型（121）

### 月之暗面（3 条重点）

- [moonshotai/Kimi-K3.1-Pro updated](https://huggingface.co/moonshotai/Kimi-K3.1-Pro)
  - 中文说明：主体：月之暗面；事件类型：模型发布；来源：Hugging Face 模型流；评分：100.55；标签：8-bit、编程、compressed-tensors、conversational、custom_code、endpoints_compatible、eval-results、图像、image-text-to-text、kimi_k31、license:other、region:us、safetensors、text-generation、transformers。
  - 摘要：`moonshotai/Kimi-K3.1-Pro` 的 Hugging Face 模型页最近发生了更新，通常对应新权重、量化版本、模型卡或可用性变化。 当前可见下载量约 83996，点赞约 2504。
  - 推荐理由：模型分发页显示下载量约 83996；社区点赞约 2504；这是模型层面的直接更新信号，不是二手媒体转述
  - 关键信号：标签：transformers / safetensors / kimi_k31 / text-generation / compressed-tensors / conversational；下载量：83996；点赞：2504；信号来源：Hugging Face 模型页
  - 原文摘要：tags=transformers, safetensors, kimi_k31, text-generation, compressed-tensors, conversational; downloads=83996; likes=2504

- [moonshotai/Kimi-K3 updated](https://huggingface.co/moonshotai/Kimi-K3)
  - 中文说明：主体：月之暗面；事件类型：模型发布；来源：Hugging Face 模型流；评分：97.39；标签：8-bit、编程、compressed-tensors、conversational、custom_code、deploy:sagemaker、eval-results、feature-extraction、图像、image-text-to-text、kimi_k3、license:other、region:us、safetensors、transformers。
  - 摘要：`moonshotai/Kimi-K3` 的 Hugging Face 模型页最近发生了更新，通常对应新权重、量化版本、模型卡或可用性变化。 当前可见下载量约 674720，点赞约 12027。
  - 推荐理由：模型分发页显示下载量约 674720；社区点赞约 12027；这是模型层面的直接更新信号，不是二手媒体转述
  - 关键信号：标签：transformers / safetensors / kimi_k3 / feature-extraction / compressed-tensors / conversational；下载量：674720；点赞：12027；信号来源：Hugging Face 模型页
  - 原文摘要：tags=transformers, safetensors, kimi_k3, feature-extraction, compressed-tensors, conversational; downloads=674720; likes=12027

- [moonshotai/Kimi-K2.5 updated](https://huggingface.co/moonshotai/Kimi-K2.5)
  - 中文说明：主体：月之暗面；事件类型：模型发布；来源：Hugging Face 模型流；评分：85.00；标签：arxiv:2602.02276、编程、compressed-tensors、conversational、custom_code、deploy:sagemaker、eval-results、feature-extraction、图像、image-text-to-text、kimi_k25、license:other、region:us、safetensors、transformers。
  - 摘要：`moonshotai/Kimi-K2.5` 的 Hugging Face 模型页最近发生了更新，通常对应新权重、量化版本、模型卡或可用性变化。 当前可见下载量约 316211，点赞约 2903。
  - 推荐理由：模型分发页显示下载量约 316211；社区点赞约 2903；这是模型层面的直接更新信号，不是二手媒体转述
  - 关键信号：标签：transformers / safetensors / kimi_k25 / feature-extraction / compressed-tensors / image-text-to-text；下载量：316211；点赞：2903；信号来源：Hugging Face 模型页
  - 原文摘要：tags=transformers, safetensors, kimi_k25, feature-extraction, compressed-tensors, image-text-to-text; downloads=316211; likes=2903

### MiniMax（3 条重点）

- [MiniMaxAI/MiniMax-H3 updated](https://huggingface.co/MiniMaxAI/MiniMax-H3)
  - 中文说明：主体：MiniMax；事件类型：模型发布；来源：Hugging Face 模型流；评分：96.87；标签：audio-to-audio-video、audio-video-generation、de、diffusers、en、es、fr、图像、image-text-to-audio-video、image-text-to-video、image-to-audio-video、image-to-video、license:other、minimax-h3、多模态、nl、reference-to-audio-video、region:us、safetensors、sv、synchronized-audio-video、text-to-audio-video、text-to-video、视频、video-to-audio-video、video-to-video、语音。
  - 摘要：`MiniMaxAI/MiniMax-H3` 的 Hugging Face 模型页最近发生了更新，通常对应新权重、量化版本、模型卡或可用性变化。 当前可见下载量约 6012871，点赞约 7374。
  - 推荐理由：模型分发页显示下载量约 6012871；社区点赞约 7374；这是模型层面的直接更新信号，不是二手媒体转述
  - 关键信号：标签：minimax-h3 / diffusers / safetensors / text-to-video / image-to-video / image-text-to-video；下载量：6012871；点赞：7374；信号来源：Hugging Face 模型页
  - 原文摘要：tags=minimax-h3, diffusers, safetensors, text-to-video, image-to-video, image-text-to-video; downloads=6012871; likes=7374

- [MiniMaxAI/MiniMax-M2 updated](https://huggingface.co/MiniMaxAI/MiniMax-M2)
  - 中文说明：主体：MiniMax；事件类型：模型发布；来源：Hugging Face 模型流；评分：85.00；标签：arxiv:2504.07164、arxiv:2509.06501、arxiv:2509.13160、编程、conversational、custom_code、deploy:azure、deploy:sagemaker、endpoints_compatible、eval-results、fp8、license:other、minimax_m2、region:us、safetensors、text-generation、transformers。
  - 摘要：`MiniMaxAI/MiniMax-M2` 的 Hugging Face 模型页最近发生了更新，通常对应新权重、量化版本、模型卡或可用性变化。 当前可见下载量约 110631，点赞约 1512。
  - 推荐理由：模型分发页显示下载量约 110631；社区点赞约 1512；这是模型层面的直接更新信号，不是二手媒体转述
  - 关键信号：标签：transformers / safetensors / minimax_m2 / text-generation / conversational / custom_code；下载量：110631；点赞：1512；信号来源：Hugging Face 模型页
  - 原文摘要：tags=transformers, safetensors, minimax_m2, text-generation, conversational, custom_code; downloads=110631; likes=1512

- [MiniMaxAI/MiniMax-M2.1 updated](https://huggingface.co/MiniMaxAI/MiniMax-M2.1)
  - 中文说明：主体：MiniMax；事件类型：模型发布；来源：Hugging Face 模型流；评分：85.00；标签：arxiv:2509.06501、编程、conversational、custom_code、deploy:azure、deploy:sagemaker、endpoints_compatible、eval-results、fp8、license:other、minimax_m2、region:us、safetensors、text-generation、transformers。
  - 摘要：`MiniMaxAI/MiniMax-M2.1` 的 Hugging Face 模型页最近发生了更新，通常对应新权重、量化版本、模型卡或可用性变化。 当前可见下载量约 13204，点赞约 1372。
  - 推荐理由：模型分发页显示下载量约 13204；社区点赞约 1372；这是模型层面的直接更新信号，不是二手媒体转述
  - 关键信号：标签：transformers / safetensors / minimax_m2 / text-generation / conversational / custom_code；下载量：13204；点赞：1372；信号来源：Hugging Face 模型页
  - 原文摘要：tags=transformers, safetensors, minimax_m2, text-generation, conversational, custom_code; downloads=13204; likes=1372

### Mistral AI（3 条重点）

- [mistralai/Leanstral-1.5-119B-A6B updated](https://huggingface.co/mistralai/Leanstral-1.5-119B-A6B)
  - 中文说明：主体：Mistral AI；事件类型：模型发布；来源：Hugging Face 模型流；评分：89.53；标签：base_model:finetune:mistralai/Leanstral-2603、base_model:mistralai/Leanstral-2603、license:apache-2.0、region:us、vllm。
  - 摘要：`mistralai/Leanstral-1.5-119B-A6B` 的 Hugging Face 模型页最近发生了更新，通常对应新权重、量化版本、模型卡或可用性变化。 当前可见下载量约 446，点赞约 235。
  - 推荐理由：模型分发页显示下载量约 446；社区点赞约 235；这是模型层面的直接更新信号，不是二手媒体转述
  - 关键信号：标签：vllm / base_model:mistralai/Leanstral-2603 / base_model:finetune:mistralai/Leanstral-2603 / license:apache-2.0 / region:us；下载量：446；点赞：235；信号来源：Hugging Face 模型页
  - 原文摘要：tags=vllm, base_model:mistralai/Leanstral-2603, base_model:finetune:mistralai/Leanstral-2603, license:apache-2.0, region:us; downloads=446; likes=235

- [mistralai/Leanstral-2603 updated](https://huggingface.co/mistralai/Leanstral-2603)
  - 中文说明：主体：Mistral AI；事件类型：模型发布；来源：Hugging Face 模型流；评分：86.88；标签：license:apache-2.0、region:us、vllm。
  - 摘要：`mistralai/Leanstral-2603` 的 Hugging Face 模型页最近发生了更新，通常对应新权重、量化版本、模型卡或可用性变化。 当前可见下载量约 175，点赞约 182。
  - 推荐理由：模型分发页显示下载量约 175；社区点赞约 182；这是模型层面的直接更新信号，不是二手媒体转述
  - 关键信号：标签：vllm / license:apache-2.0 / region:us；下载量：175；点赞：182；信号来源：Hugging Face 模型页
  - 原文摘要：tags=vllm, license:apache-2.0, region:us; downloads=175; likes=182

- [mistralai/Mistral-Large-3-675B-Instruct-2512-NVFP4 updated](https://huggingface.co/mistralai/Mistral-Large-3-675B-Instruct-2512-NVFP4)
  - 中文说明：主体：Mistral AI；事件类型：模型发布；来源：Hugging Face 模型流；评分：82.63；标签：ar、base_model:finetune:mistralai/Mistral-Large-3-675B-Base-2512、base_model:mistralai/Mistral-Large-3-675B-Base-2512、compressed-tensors、de、en、es、fr、it、ja、ko、license:apache-2.0、mistral-common、nl、pt、region:us、vllm、zh。
  - 摘要：`mistralai/Mistral-Large-3-675B-Instruct-2512-NVFP4` 的 Hugging Face 模型页最近发生了更新，通常对应新权重、量化版本、模型卡或可用性变化。 当前可见下载量约 5994，点赞约 97。
  - 推荐理由：模型分发页显示下载量约 5994；社区点赞约 97；这是模型层面的直接更新信号，不是二手媒体转述
  - 关键信号：标签：vllm / mistral-common / compressed-tensors / en / fr / es；下载量：5994；点赞：97；信号来源：Hugging Face 模型页
  - 原文摘要：tags=vllm, mistral-common, compressed-tensors, en, fr, es; downloads=5994; likes=97

### InternLM（3 条重点）

- [internlm/Sage-S2.1-Flash updated](https://huggingface.co/internlm/Sage-S2.1-Flash)
  - 中文说明：主体：InternLM；事件类型：模型发布；来源：Hugging Face 模型流；评分：88.54；标签：arxiv:2611.21072、eval-results、glm5_next、region:us、safetensors。
  - 摘要：`internlm/Sage-S2.1-Flash` 的 Hugging Face 模型页最近发生了更新，通常对应新权重、量化版本、模型卡或可用性变化。 当前可见下载量约 1694，点赞约 319。
  - 推荐理由：模型分发页显示下载量约 1694；社区点赞约 319；这是模型层面的直接更新信号，不是二手媒体转述
  - 关键信号：标签：safetensors / glm5_next / arxiv:2611.21072 / eval-results / region:us；下载量：1694；点赞：319；信号来源：Hugging Face 模型页
  - 原文摘要：tags=safetensors, glm5_next, arxiv:2611.21072, eval-results, region:us; downloads=1694; likes=319

- [internlm/Sage-Interaction updated](https://huggingface.co/internlm/Sage-Interaction)
  - 中文说明：主体：InternLM；事件类型：模型发布；来源：Hugging Face 模型流；评分：78.01；标签：any-to-any、编程、custom_code、feature-extraction、full-duplex、minicpmo、多模态、onnx、region:us、safetensors、streaming、task-delegation、transformers。
  - 摘要：`internlm/Sage-Interaction` 的 Hugging Face 模型页最近发生了更新，通常对应新权重、量化版本、模型卡或可用性变化。 当前可见下载量约 1，点赞约 16。
  - 推荐理由：模型分发页显示下载量约 1；社区点赞约 16；这是模型层面的直接更新信号，不是二手媒体转述
  - 关键信号：标签：transformers / onnx / safetensors / minicpmo / feature-extraction / multimodal；下载量：1；点赞：16；信号来源：Hugging Face 模型页
  - 原文摘要：tags=transformers, onnx, safetensors, minicpmo, feature-extraction, multimodal; downloads=1; likes=16

- [internlm/Sage-S2.1-Flash-FP8 updated](https://huggingface.co/internlm/Sage-S2.1-Flash-FP8)
  - 中文说明：主体：InternLM；事件类型：模型发布；来源：Hugging Face 模型流；评分：73.66；标签：arxiv:2611.21072、fp8、glm5_next、region:us、safetensors。
  - 摘要：`internlm/Sage-S2.1-Flash-FP8` 的 Hugging Face 模型页最近发生了更新，通常对应新权重、量化版本、模型卡或可用性变化。 当前可见下载量约 747，点赞约 20。
  - 推荐理由：模型分发页显示下载量约 747；社区点赞约 20；这是模型层面的直接更新信号，不是二手媒体转述
  - 关键信号：标签：safetensors / glm5_next / arxiv:2611.21072 / fp8 / region:us；下载量：747；点赞：20；信号来源：Hugging Face 模型页
  - 原文摘要：tags=safetensors, glm5_next, arxiv:2611.21072, fp8, region:us; downloads=747; likes=20

### Qwen（3 条重点）

- [Qwen/Qwen2-VL-2B-Instruct updated](https://huggingface.co/Qwen/Qwen2-VL-2B-Instruct)
  - 中文说明：主体：Qwen；事件类型：模型发布；来源：Hugging Face 模型流；评分：85.00；标签：arxiv:2308.12966、arxiv:2409.12191、base_model:Qwen/Qwen2-VL-2B、base_model:finetune:Qwen/Qwen2-VL-2B、conversational、deploy:azure、en、endpoints_compatible、图像、image-text-to-text、基础设施、license:apache-2.0、多模态、qwen2_vl、region:us、safetensors、text-generation-inference、transformers。
  - 摘要：`Qwen/Qwen2-VL-2B-Instruct` 的 Hugging Face 模型页最近发生了更新，通常对应新权重、量化版本、模型卡或可用性变化。 当前可见下载量约 910097，点赞约 533。
  - 推荐理由：模型分发页显示下载量约 910097；社区点赞约 533；这是模型层面的直接更新信号，不是二手媒体转述
  - 关键信号：标签：transformers / safetensors / qwen2_vl / image-text-to-text / multimodal / conversational；下载量：910097；点赞：533；信号来源：Hugging Face 模型页
  - 原文摘要：tags=transformers, safetensors, qwen2_vl, image-text-to-text, multimodal, conversational; downloads=910097; likes=533

- [Qwen/Qwen3.6-27B updated](https://huggingface.co/Qwen/Qwen3.6-27B)
  - 中文说明：主体：Qwen；事件类型：模型发布；来源：Hugging Face 模型流；评分：85.00；标签：conversational、deploy:azure、deploy:sagemaker、endpoints_compatible、eval-results、图像、image-text-to-text、license:apache-2.0、qwen3_5、region:us、safetensors、transformers。
  - 摘要：`Qwen/Qwen3.6-27B` 的 Hugging Face 模型页最近发生了更新，通常对应新权重、量化版本、模型卡或可用性变化。 当前可见下载量约 2286448，点赞约 2364。
  - 推荐理由：模型分发页显示下载量约 2286448；社区点赞约 2364；这是模型层面的直接更新信号，不是二手媒体转述
  - 关键信号：标签：transformers / safetensors / qwen3_5 / image-text-to-text / conversational / license:apache-2.0；下载量：2286448；点赞：2364；信号来源：Hugging Face 模型页
  - 原文摘要：tags=transformers, safetensors, qwen3_5, image-text-to-text, conversational, license:apache-2.0; downloads=2286448; likes=2364

- [Qwen/Qwen3.5-27B updated](https://huggingface.co/Qwen/Qwen3.5-27B)
  - 中文说明：主体：Qwen；事件类型：模型发布；来源：Hugging Face 模型流；评分：85.00；标签：conversational、deploy:azure、deploy:sagemaker、endpoints_compatible、eval-results、图像、image-text-to-text、license:apache-2.0、qwen3_5、region:us、safetensors、transformers。
  - 摘要：`Qwen/Qwen3.5-27B` 的 Hugging Face 模型页最近发生了更新，通常对应新权重、量化版本、模型卡或可用性变化。 当前可见下载量约 1452867，点赞约 1099。
  - 推荐理由：模型分发页显示下载量约 1452867；社区点赞约 1099；这是模型层面的直接更新信号，不是二手媒体转述
  - 关键信号：标签：transformers / safetensors / qwen3_5 / image-text-to-text / conversational / license:apache-2.0；下载量：1452867；点赞：1099；信号来源：Hugging Face 模型页
  - 原文摘要：tags=transformers, safetensors, qwen3_5, image-text-to-text, conversational, license:apache-2.0; downloads=1452867; likes=1099

### DeepSeek（3 条重点）

- [deepseek-ai/DeepSeek-V4.1-Flash-1017 updated](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)
  - 中文说明：主体：DeepSeek；事件类型：模型发布；来源：Hugging Face 模型流；评分：85.00；标签：8-bit、conversational、deepseek_v41、deploy:azure、endpoints_compatible、eval-results、fp8、图像、image-text-to-text、license:mit、region:us、safetensors、text-generation、transformers。
  - 摘要：`deepseek-ai/DeepSeek-V4.1-Flash-1017` 的 Hugging Face 模型页最近发生了更新，通常对应新权重、量化版本、模型卡或可用性变化。 当前可见下载量约 550396，点赞约 6704。
  - 推荐理由：模型分发页显示下载量约 550396；社区点赞约 6704；这是模型层面的直接更新信号，不是二手媒体转述
  - 关键信号：标签：transformers / safetensors / deepseek_v41 / text-generation / image-text-to-text / conversational；下载量：550396；点赞：6704；信号来源：Hugging Face 模型页
  - 原文摘要：tags=transformers, safetensors, deepseek_v41, text-generation, image-text-to-text, conversational; downloads=550396; likes=6704

- [deepseek-ai/DeepSeek-V4.1-Flash updated](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
  - 中文说明：主体：DeepSeek；事件类型：模型发布；来源：Hugging Face 模型流；评分：85.00；标签：8-bit、conversational、deepseek_v41、deploy:azure、deploy:sagemaker、endpoints_compatible、eval-results、fp8、图像、image-text-to-text、license:mit、region:us、safetensors、text-generation、transformers。
  - 摘要：`deepseek-ai/DeepSeek-V4.1-Flash` 的 Hugging Face 模型页最近发生了更新，通常对应新权重、量化版本、模型卡或可用性变化。 当前可见下载量约 1096257，点赞约 5107。
  - 推荐理由：模型分发页显示下载量约 1096257；社区点赞约 5107；这是模型层面的直接更新信号，不是二手媒体转述
  - 关键信号：标签：transformers / safetensors / deepseek_v41 / text-generation / image-text-to-text / conversational；下载量：1096257；点赞：5107；信号来源：Hugging Face 模型页
  - 原文摘要：tags=transformers, safetensors, deepseek_v41, text-generation, image-text-to-text, conversational; downloads=1096257; likes=5107

- [deepseek-ai/DeepSeek-V4-Flash-Vision-Exp updated](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp)
  - 中文说明：主体：DeepSeek；事件类型：模型发布；来源：Hugging Face 模型流；评分：85.00；标签：8-bit、deepseek_v4、endpoints_compatible、eval-results、fp8、图像、image-text-to-text、license:mit、region:us、safetensors、text-generation、transformers。
  - 摘要：`deepseek-ai/DeepSeek-V4-Flash-Vision-Exp` 的 Hugging Face 模型页最近发生了更新，通常对应新权重、量化版本、模型卡或可用性变化。 当前可见下载量约 28206，点赞约 972。
  - 推荐理由：模型分发页显示下载量约 28206；社区点赞约 972；这是模型层面的直接更新信号，不是二手媒体转述
  - 关键信号：标签：transformers / safetensors / deepseek_v4 / text-generation / image-text-to-text / license:mit；下载量：28206；点赞：972；信号来源：Hugging Face 模型页
  - 原文摘要：tags=transformers, safetensors, deepseek_v4, text-generation, image-text-to-text, license:mit; downloads=28206; likes=972

## 新开源项目（100）

### DeepSeek（3 条重点）

- [deepseek-ai/deepseek-harness is trending](https://github.com/deepseek-ai/deepseek-harness)
  - 中文说明：主体：DeepSeek；事件类型：开源项目发布；来源：GitHub 发现流；评分：76.00；标签：未打标签。
  - 摘要：`deepseek-ai/deepseek-harness` 最近进入 GitHub 高活跃区间，属于用于扩展现有 AI 系统能力的插件或集成项目。DeepSeek Harness: Everything is a Plugin.
  - 推荐理由：当前 GitHub stars 约 287176，已不是早期小项目；近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度；属于近 24 小时内的新鲜动态
  - 关键信号：开源类型：用于扩展现有 AI 系统能力的插件或集成项目；GitHub stars：287176；信号来源：GitHub 发现流。
  - 原文摘要：DeepSeek Harness: Everything is a Plugin.

- [deepseek-ai/DeepSelect is trending](https://github.com/deepseek-ai/DeepSelect)
  - 中文说明：主体：DeepSeek；事件类型：开源项目发布；来源：GitHub 发现流；评分：75.91；标签：未打标签。
  - 摘要：`deepseek-ai/DeepSelect` 最近进入 GitHub 高活跃区间，属于面向 AI 应用或基础设施的开源项目。DeepSelect: TopK kernels for DeepSeek Sparse Attention (DSA) and Samplers
  - 推荐理由：当前 GitHub stars 约 557，说明已经形成一定关注度；近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度；属于近 24 小时内的新鲜动态
  - 关键信号：开源类型：面向 AI 应用或基础设施的开源项目；GitHub stars：557；信号来源：GitHub 发现流。
  - 原文摘要：DeepSelect: TopK kernels for DeepSeek Sparse Attention (DSA) and Samplers

- [deepseek-ai/chat-demo is trending](https://github.com/deepseek-ai/chat-demo)
  - 中文说明：主体：DeepSeek；事件类型：开源项目发布；来源：GitHub 发现流；评分：75.83；标签：未打标签。
  - 摘要：`deepseek-ai/chat-demo` 最近进入 GitHub 高活跃区间，属于面向 AI 应用或基础设施的开源项目。Chat Demo
  - 推荐理由：当前 GitHub stars 约 5463，已不是早期小项目；近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度；属于近 24 小时内的新鲜动态
  - 关键信号：开源类型：面向 AI 应用或基础设施的开源项目；GitHub stars：5463；信号来源：GitHub 发现流。
  - 原文摘要：Chat Demo

### ThreatDefence（1 条重点）

- [ThreatDefence/agentic-attack-detections is trending](https://github.com/ThreatDefence/agentic-attack-detections)
  - 中文说明：主体：ThreatDefence；事件类型：开源项目发布；来源：GitHub 发现流；评分：76.00；标签：Agent。
  - 摘要：`ThreatDefence/agentic-attack-detections` 最近进入 GitHub 高活跃区间，属于面向 AI agent 或编码助手的开源项目。Detection rules and IOCs for AI agent attack frameworks: ARTEX, Cairn, PentAGI, HexStrike, CyberStrikeAI, Strix, Hermes…
  - 推荐理由：当前 GitHub stars 约 714，说明已经形成一定关注度；近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度；属于近 24 小时内的新鲜动态
  - 关键信号：开源类型：面向 AI agent 或编码助手的开源项目；GitHub stars：714；信号来源：GitHub 发现流。
  - 原文摘要：Detection rules and IOCs for AI agent attack frameworks: ARTEX, Cairn, PentAGI, HexStrike, CyberStrikeAI, Strix, Hermes Agent, Agent Zero, RedAmon, Xalgorix, Pentest Swarm AI. KQL…

### ModelScope（3 条重点）

- [modelscope/ms-swift is trending](https://github.com/modelscope/ms-swift)
  - 中文说明：主体：ModelScope；事件类型：开源项目发布；来源：GitHub 发现流；评分：75.95；标签：未打标签。
  - 摘要：`modelscope/ms-swift` 最近进入 GitHub 高活跃区间，属于围绕模型权重、模型推理或模型家族的开源项目。Use PEFT or Full-parameter to CPT/SFT/DPO/GRPO 600+ LLMs (Qwen3.8, DeepSeek-V4, GLM-5.1, InternLM3, Llama4, ...) and 30…
  - 推荐理由：当前 GitHub stars 约 16174，已不是早期小项目；近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度；属于近 24 小时内的新鲜动态
  - 关键信号：开源类型：围绕模型权重、模型推理或模型家族的开源项目；GitHub stars：16174；信号来源：GitHub 发现流。
  - 原文摘要：Use PEFT or Full-parameter to CPT/SFT/DPO/GRPO 600+ LLMs (Qwen3.8, DeepSeek-V4, GLM-5.1, InternLM3, Llama4, ...) and 300+ MLLMs (Qwen3-VL, Qwen3-Omni, InternVL3.5, Ovis2.5, GLM5.3…

- [modelscope/FunASR is trending](https://github.com/modelscope/FunASR)
  - 中文说明：主体：ModelScope；事件类型：开源项目发布；来源：GitHub 发现流；评分：75.84；标签：语音、基础设施。
  - 摘要：`modelscope/FunASR` 最近进入 GitHub 高活跃区间，属于用于语音处理或语音识别的开源项目。Open-source speech recognition toolkit for training, inference, streaming ASR, VAD, punctuation, speaker diarization pi…
  - 推荐理由：当前 GitHub stars 约 21134，已不是早期小项目；近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度；属于近 24 小时内的新鲜动态
  - 关键信号：开源类型：用于语音处理或语音识别的开源项目；GitHub stars：21134；信号来源：GitHub 发现流。
  - 原文摘要：Open-source speech recognition toolkit for training, inference, streaming ASR, VAD, punctuation, speaker diarization pipelines, and OpenAI-compatible/MCP serving.

- [modelscope/ms-cookbook is trending](https://github.com/modelscope/ms-cookbook)
  - 中文说明：主体：ModelScope；事件类型：开源项目发布；来源：GitHub 发现流；评分：75.56；标签：Agent。
  - 摘要：`modelscope/ms-cookbook` 最近进入 GitHub 高活跃区间，属于面向 AI agent 或编码助手的开源项目。魔搭紫皮书｜ModelScope Cookbook：面向开发者的开源模型应用实战指南，覆盖模型选型、推理、微调、评测、RAG、Agent 与 AIGC，从跑通第一个模型到构建实际应用。
  - 推荐理由：当前 GitHub stars 约 546，说明已经形成一定关注度；近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度；属于近 24 小时内的新鲜动态
  - 关键信号：开源类型：面向 AI agent 或编码助手的开源项目；GitHub stars：546；信号来源：GitHub 发现流。
  - 原文摘要：魔搭紫皮书｜ModelScope Cookbook：面向开发者的开源模型应用实战指南，覆盖模型选型、推理、微调、评测、RAG、Agent 与 AIGC，从跑通第一个模型到构建实际应用。

### sous-labs（1 条重点）

- [sous-labs/songe is trending](https://github.com/sous-labs/songe)
  - 中文说明：主体：sous-labs；事件类型：开源项目发布；来源：GitHub 发现流；评分：75.92；标签：未打标签。
  - 摘要：`sous-labs/songe` 最近进入 GitHub 高活跃区间，属于围绕模型权重、模型推理或模型家族的开源项目。A training engine for your local model, using your idle compute
  - 推荐理由：当前 GitHub stars 约 876，说明已经形成一定关注度；近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度；属于近 24 小时内的新鲜动态
  - 关键信号：开源类型：围绕模型权重、模型推理或模型家族的开源项目；GitHub stars：876；信号来源：GitHub 发现流。
  - 原文摘要：A training engine for your local model, using your idle compute

### Qwen（3 条重点）

- [QwenLM/Qwen-MM-Plugins is trending](https://github.com/QwenLM/Qwen-MM-Plugins)
  - 中文说明：主体：Qwen；事件类型：开源项目发布；来源：GitHub 发现流；评分：75.91；标签：Agent、多模态。
  - 摘要：`QwenLM/Qwen-MM-Plugins` 最近进入 GitHub 高活跃区间，属于面向 AI agent 或编码助手的开源项目。Make any agent harness multimodal-native.
  - 推荐理由：当前 GitHub stars 约 3213，说明已经形成一定关注度；近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度；属于近 24 小时内的新鲜动态
  - 关键信号：开源类型：面向 AI agent 或编码助手的开源项目；GitHub stars：3213；信号来源：GitHub 发现流。
  - 原文摘要：Make any agent harness multimodal-native.

- [QwenLM/FlashQLA is trending](https://github.com/QwenLM/FlashQLA)
  - 中文说明：主体：Qwen；事件类型：开源项目发布；来源：GitHub 发现流；评分：75.73；标签：未打标签。
  - 摘要：`QwenLM/FlashQLA` 最近进入 GitHub 高活跃区间，属于面向 AI 应用或基础设施的开源项目。high-performance linear attention kernel library built on TileLang
  - 推荐理由：当前 GitHub stars 约 772，说明已经形成一定关注度；近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度；属于近 24 小时内的新鲜动态
  - 关键信号：开源类型：面向 AI 应用或基础设施的开源项目；GitHub stars：772；信号来源：GitHub 发现流。
  - 原文摘要：high-performance linear attention kernel library built on TileLang

- [QwenLM/qwen-code is trending](https://github.com/QwenLM/qwen-code)
  - 中文说明：主体：Qwen；事件类型：开源项目发布；来源：GitHub 发现流；评分：75.62；标签：Agent、编程。
  - 摘要：`QwenLM/qwen-code` 最近进入 GitHub 高活跃区间，属于面向 AI agent 或编码助手的开源项目。An open-source AI coding agent that lives in your terminal.
  - 推荐理由：当前 GitHub stars 约 30949，已不是早期小项目；近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度；属于近 24 小时内的新鲜动态
  - 关键信号：开源类型：面向 AI agent 或编码助手的开源项目；GitHub stars：30949；信号来源：GitHub 发现流。
  - 原文摘要：An open-source AI coding agent that lives in your terminal.

### Tencent Hunyuan（3 条重点）

- [Tencent-Hunyuan/Hy-Memory is trending](https://github.com/Tencent-Hunyuan/Hy-Memory)
  - 中文说明：主体：Tencent Hunyuan；事件类型：开源项目发布；来源：GitHub 发现流；评分：75.83；标签：未打标签。
  - 摘要：`Tencent-Hunyuan/Hy-Memory` 最近进入 GitHub 高活跃区间，属于面向 AI 应用或基础设施的开源项目。当前公开描述较少。
  - 推荐理由：当前 GitHub stars 约 2114，说明已经形成一定关注度；近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度；属于近 24 小时内的新鲜动态
  - 关键信号：开源类型：面向 AI 应用或基础设施的开源项目；GitHub stars：2114；信号来源：GitHub 发现流。

- [Tencent-Hunyuan/HunyuanWorld-Mirror is trending](https://github.com/Tencent-Hunyuan/HunyuanWorld-Mirror)
  - 中文说明：主体：Tencent Hunyuan；事件类型：开源项目发布；来源：GitHub 发现流；评分：75.47；标签：未打标签。
  - 摘要：`Tencent-Hunyuan/HunyuanWorld-Mirror` 最近进入 GitHub 高活跃区间，属于围绕模型权重、模型推理或模型家族的开源项目。[ICML 2026] WorldMirror: Fast and Universal 3D reconstruction model for versatile tasks
  - 推荐理由：当前 GitHub stars 约 1235，说明已经形成一定关注度；近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度；属于近 24 小时内的新鲜动态
  - 关键信号：开源类型：围绕模型权重、模型推理或模型家族的开源项目；GitHub stars：1235；信号来源：GitHub 发现流。
  - 原文摘要：[ICML 2026] WorldMirror: Fast and Universal 3D reconstruction model for versatile tasks

- [Tencent-Hunyuan/UniRL is trending](https://github.com/Tencent-Hunyuan/UniRL)
  - 中文说明：主体：Tencent Hunyuan；事件类型：开源项目发布；来源：GitHub 发现流；评分：74.55；标签：多模态。
  - 摘要：`Tencent-Hunyuan/UniRL` 最近进入 GitHub 高活跃区间，属于围绕模型权重、模型推理或模型家族的开源项目。UniRL is a Framework for Unified Multimodal Model Reinforcement Learning
  - 推荐理由：当前 GitHub stars 约 1052，说明已经形成一定关注度；近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度；属于近 24 小时内的新鲜动态
  - 关键信号：开源类型：围绕模型权重、模型推理或模型家族的开源项目；GitHub stars：1052；信号来源：GitHub 发现流。
  - 原文摘要：UniRL is a Framework for Unified Multimodal Model Reinforcement Learning

### 月之暗面（3 条重点）

- [MoonshotAI/kimi-code is trending](https://github.com/MoonshotAI/kimi-code)
  - 中文说明：主体：月之暗面；事件类型：开源项目发布；来源：GitHub 发现流；评分：75.83；标签：Agent、编程。
  - 摘要：`MoonshotAI/kimi-code` 最近进入 GitHub 高活跃区间，属于面向 AI agent 或编码助手的开源项目。Kimi Code CLI — The Starting Point for Next-Gen Agents
  - 推荐理由：当前 GitHub stars 约 8294，已不是早期小项目；近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度；属于近 24 小时内的新鲜动态
  - 关键信号：开源类型：面向 AI agent 或编码助手的开源项目；GitHub stars：8294；信号来源：GitHub 发现流。
  - 原文摘要：Kimi Code CLI — The Starting Point for Next-Gen Agents

- [MoonshotAI/FlashKDA is trending](https://github.com/MoonshotAI/FlashKDA)
  - 中文说明：主体：月之暗面；事件类型：开源项目发布；来源：GitHub 发现流；评分：75.03；标签：未打标签。
  - 摘要：`MoonshotAI/FlashKDA` 最近进入 GitHub 高活跃区间，属于面向 AI 应用或基础设施的开源项目。FlashKDA: high-performance Kimi Delta Attention kernels
  - 推荐理由：当前 GitHub stars 约 1303，说明已经形成一定关注度；近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度；属于近 24 小时内的新鲜动态
  - 关键信号：开源类型：面向 AI 应用或基础设施的开源项目；GitHub stars：1303；信号来源：GitHub 发现流。
  - 原文摘要：FlashKDA: high-performance Kimi Delta Attention kernels

- [MoonshotAI/MoonEP is trending](https://github.com/MoonshotAI/MoonEP)
  - 中文说明：主体：月之暗面；事件类型：开源项目发布；来源：GitHub 发现流；评分：73.58；标签：未打标签。
  - 摘要：`MoonshotAI/MoonEP` 最近进入 GitHub 高活跃区间，属于面向 AI 应用或基础设施的开源项目。MoonEP: A Perfectly Balanced Expert Parallelism Library via Dynamic Redundant Experts
  - 推荐理由：当前 GitHub stars 约 1220，说明已经形成一定关注度；近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度；属于近 24 小时内的新鲜动态
  - 关键信号：开源类型：面向 AI 应用或基础设施的开源项目；GitHub stars：1220；信号来源：GitHub 发现流。
  - 原文摘要：MoonEP: A Perfectly Balanced Expert Parallelism Library via Dynamic Redundant Experts

### ByteDance Seed（3 条重点）

- [ByteDance-Seed/Triton-distributed is trending](https://github.com/ByteDance-Seed/Triton-distributed)
  - 中文说明：主体：ByteDance Seed；事件类型：开源项目发布；来源：GitHub 发现流；评分：75.71；标签：未打标签。
  - 摘要：`ByteDance-Seed/Triton-distributed` 最近进入 GitHub 高活跃区间，属于面向 AI 应用或基础设施的开源项目。Distributed Compiler and Optimized Parallel Kernels
  - 推荐理由：当前 GitHub stars 约 1591，说明已经形成一定关注度；近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度；属于近 24 小时内的新鲜动态
  - 关键信号：开源类型：面向 AI 应用或基础设施的开源项目；GitHub stars：1591；信号来源：GitHub 发现流。
  - 原文摘要：Distributed Compiler and Optimized Parallel Kernels

- [ByteDance-Seed/VeOmni is trending](https://github.com/ByteDance-Seed/VeOmni)
  - 中文说明：主体：ByteDance Seed；事件类型：开源项目发布；来源：GitHub 发现流；评分：74.52；标签：未打标签。
  - 摘要：`ByteDance-Seed/VeOmni` 最近进入 GitHub 高活跃区间，属于围绕模型权重、模型推理或模型家族的开源项目。VeOmni: Scaling Any Modality Model Training with Model-Centric Distributed Recipe Zoo
  - 推荐理由：当前 GitHub stars 约 2304，说明已经形成一定关注度；近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度；属于近 24 小时内的新鲜动态
  - 关键信号：开源类型：围绕模型权重、模型推理或模型家族的开源项目；GitHub stars：2304；信号来源：GitHub 发现流。
  - 原文摘要：VeOmni: Scaling Any Modality Model Training with Model-Centric Distributed Recipe Zoo

- [ByteDance-Seed/EdgeBench is trending](https://github.com/ByteDance-Seed/EdgeBench)
  - 中文说明：主体：ByteDance Seed；事件类型：开源项目发布；来源：GitHub 发现流；评分：72.39；标签：未打标签。
  - 摘要：`ByteDance-Seed/EdgeBench` 最近进入 GitHub 高活跃区间，属于面向 AI 应用或基础设施的开源项目。EdgeBench: Unveiling scaling laws of learning from real-world environments
  - 推荐理由：近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度；属于近 24 小时内的新鲜动态
  - 关键信号：开源类型：面向 AI 应用或基础设施的开源项目；GitHub stars：485；信号来源：GitHub 发现流。
  - 原文摘要：EdgeBench: Unveiling scaling laws of learning from real-world environments

### MiniMax（3 条重点）

- [MiniMax-AI/MSA is trending](https://github.com/MiniMax-AI/MSA)
  - 中文说明：主体：MiniMax；事件类型：开源项目发布；来源：GitHub 发现流；评分：75.39；标签：未打标签。
  - 摘要：`MiniMax-AI/MSA` 最近进入 GitHub 高活跃区间，属于面向 AI 应用或基础设施的开源项目。当前公开描述较少。
  - 推荐理由：近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度；属于近 24 小时内的新鲜动态
  - 关键信号：开源类型：面向 AI 应用或基础设施的开源项目；GitHub stars：441；信号来源：GitHub 发现流。

- [MiniMax-AI/minimax-code is trending](https://github.com/MiniMax-AI/minimax-code)
  - 中文说明：主体：MiniMax；事件类型：开源项目发布；来源：GitHub 发现流；评分：74.19；标签：Agent、编程。
  - 摘要：`MiniMax-AI/minimax-code` 最近进入 GitHub 高活跃区间，属于面向 AI agent 或编码助手的开源项目。An open-source coding agent for your terminal, powered by MiniMax.
  - 推荐理由：当前 GitHub stars 约 2288，说明已经形成一定关注度；近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度；属于近 24 小时内的新鲜动态
  - 关键信号：开源类型：面向 AI agent 或编码助手的开源项目；GitHub stars：2288；信号来源：GitHub 发现流。
  - 原文摘要：An open-source coding agent for your terminal, powered by MiniMax.

- [MiniMax-AI/OpenAgentCore is trending](https://github.com/MiniMax-AI/OpenAgentCore)
  - 中文说明：主体：MiniMax；事件类型：开源项目发布；来源：GitHub 发现流；评分：73.56；标签：Agent、编程、基础设施。
  - 摘要：`MiniMax-AI/OpenAgentCore` 最近进入 GitHub 高活跃区间，属于面向 AI agent 或编码助手的开源项目。The OpenAI Agents API, open source and self-hosted. Run Codex, Claude Code or MiniMax Code on your own machines with yo…
  - 推荐理由：近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度；属于近 24 小时内的新鲜动态
  - 关键信号：开源类型：面向 AI agent 或编码助手的开源项目；GitHub stars：352；信号来源：GitHub 发现流。
  - 原文摘要：The OpenAI Agents API, open source and self-hosted. Run Codex, Claude Code or MiniMax Code on your own machines with your own models, through the official OpenAI SDK.

### OpenAI（3 条重点）

- [openai/openai-python: v3.59.0](https://github.com/openai/openai-python/releases/tag/v3.59.0)
  - 中文说明：主体：OpenAI；事件类型：开源项目发布；来源：GitHub Release；评分：75.26；标签：Agent、基础设施。
  - 摘要：`openai/openai-python` 刚发布了一个新版本，说明这个 SDK 或开源项目最近有明确的版本更新。
  - 推荐理由：release 代表项目维护者已经给出明确版本边界，信号强于普通提交
  - 关键信号：信号来源：GitHub Release；适合优先查看 release notes、破坏性变更和版本号。
  - 原文摘要：## [3.59.0](https://github.com/openai/openai-python/compare/v3.58.0...v3.59.0) (2026-11-24) ### Features * **api:** add healthcare model IDs for Responses ([#4327](https://github.…

- [openai/openai-python: v3.58.0](https://github.com/openai/openai-python/releases/tag/v3.58.0)
  - 中文说明：主体：OpenAI；事件类型：开源项目发布；来源：GitHub Release；评分：71.21；标签：Agent、基础设施。
  - 摘要：`openai/openai-python` 刚发布了一个新版本，说明这个 SDK 或开源项目最近有明确的版本更新。
  - 推荐理由：release 代表项目维护者已经给出明确版本边界，信号强于普通提交
  - 关键信号：信号来源：GitHub Release；适合优先查看 release notes、破坏性变更和版本号。
  - 原文摘要：## [3.58.0](https://github.com/openai/openai-python/compare/v3.57.0...v3.58.0) (2026-11-23) ### Features * **api:** set and read agent session spending limits ([#4315](https://git…

- [openai/openai-python: v3.57.0](https://github.com/openai/openai-python/releases/tag/v3.57.0)
  - 中文说明：主体：OpenAI；事件类型：开源项目发布；来源：GitHub Release；评分：61.00；标签：基础设施。
  - 摘要：`openai/openai-python` 刚发布了一个新版本，说明这个 SDK 或开源项目最近有明确的版本更新。
  - 推荐理由：release 代表项目维护者已经给出明确版本边界，信号强于普通提交
  - 关键信号：信号来源：GitHub Release；适合优先查看 release notes、破坏性变更和版本号。
  - 原文摘要：## [3.57.0](https://github.com/openai/openai-python/compare/v3.56.0...v3.57.0) (2026-11-19) ### Features * **api:** support Live WebRTC standby ([#4296](https://github.com/openai/…

## 其他观察（15）

### OpenAI（3 条重点）

- [How iFood scales coding agents across 15,000 repositories](https://openai.com/business/customer-stories/ifood)
  - 中文说明：主体：OpenAI；事件类型：观察事项；来源：官方资讯源；评分：62.04；标签：Agent、编程。
  - 摘要：这是官方发布源中的一条更新，核心内容是：How iFood scales coding agents across 15,000 repositories
  - 推荐理由：来自官方发布面，可信度比二手转述更高
  - 关键信号：信号来源：官方 RSS。

- [Searching for distant planets with Astra](https://openai.com/index/searching-for-distant-planets-with-astra)
  - 中文说明：主体：OpenAI；事件类型：观察事项；来源：官方资讯源；评分：35.88；标签：编程。
  - 摘要：这是官方发布源中的一条更新，核心内容是：See how two amateur astronomers used Codex and Astra to find potential exoplanets in public data from NASA’s Kepler and…
  - 推荐理由：来自官方发布面，可信度比二手转述更高
  - 关键信号：信号来源：官方 RSS。
  - 原文摘要：See how two amateur astronomers used Codex and Astra to find potential exoplanets in public data from NASA’s Kepler and TESS space telescopes.

- [How Intentful uses dots to make more time for growth](https://openai.com/business/customer-stories/intentful-dots)
  - 中文说明：主体：OpenAI；事件类型：观察事项；来源：官方资讯源；评分：34.04；标签：未打标签。
  - 摘要：这是官方发布源中的一条更新，核心内容是：Marina Petrova’s dot Aria helps research websites and build proposals, while proactively flagging messages and resolvin…
  - 推荐理由：来自官方发布面，可信度比二手转述更高
  - 关键信号：信号来源：官方 RSS。
  - 原文摘要：Marina Petrova’s dot Aria helps research websites and build proposals, while proactively flagging messages and resolving issues.

### Tencent Hunyuan（1 条重点）

- [All news](https://www.tencent.com/newsroom/all-news/?type=media)
  - 中文说明：主体：Tencent Hunyuan；事件类型：观察事项；来源：官方网页抓取；评分：46.00；标签：未打标签。
  - 摘要：See how teamwork, leadership and global reach bring Tencent's vision and values to life.
  - 推荐理由：来自官方发布面，可信度比二手转述更高；属于近 24 小时内的新鲜动态
  - 关键信号：信号来源：厂商官网页面；动态类型：官网动态。
  - 原文摘要：See how teamwork, leadership and global reach bring Tencent's vision and values to life.

### Hugging Face（3 条重点）

- [Building on Nemotron 3.5 Parse: Open Data, Fine-Tuning, and Faster Inference](https://huggingface.co/blog/nvidia/building-on-nemotron-35-parse-open-data-fine-tunin)
  - 中文说明：主体：Hugging Face；事件类型：观察事项；来源：官方资讯源；评分：42.89；标签：基础设施。
  - 摘要：这是官方发布源中的一条更新，核心内容是：Building on Nemotron 3.5 Parse: Open Data, Fine-Tuning, and Faster Inference
  - 推荐理由：来自官方发布面，可信度比二手转述更高；属于近 24 小时内的新鲜动态
  - 关键信号：信号来源：官方 RSS。

- [Hill-climbing Inkling 2 Mini inference on one RTX PRO 6000](https://huggingface.co/blog/inkling-2-mini-inference-hillclimb)
  - 中文说明：主体：Hugging Face；事件类型：观察事项；来源：官方资讯源；评分：38.04；标签：基础设施。
  - 摘要：这是官方发布源中的一条更新，核心内容是：Hill-climbing Inkling 2 Mini inference on one RTX PRO 6000
  - 推荐理由：来自官方发布面，可信度比二手转述更高
  - 关键信号：信号来源：官方 RSS。

- [Welcome Inkling 2 Mini, Cutting-edge Performance for your Local Setup](https://huggingface.co/blog/inkling2mini)
  - 中文说明：主体：Hugging Face；事件类型：观察事项；来源：官方资讯源；评分：23.00；标签：未打标签。
  - 摘要：这是官方发布源中的一条更新，核心内容是：Welcome Inkling 2 Mini, Cutting-edge Performance for your Local Setup
  - 推荐理由：来自官方发布面，可信度比二手转述更高
  - 关键信号：信号来源：官方 RSS。

### NVIDIA AI（3 条重点）

- [Merry Making: Play, Build and Create With NVIDIA Technologies This Holiday Season](https://blogs.nvidia.com/blog/nvidia-technologies-holidays-2026/)
  - 中文说明：主体：NVIDIA AI；事件类型：观察事项；来源：官方资讯源；评分：32.88；标签：未打标签。
  - 摘要：这是官方发布源中的一条更新，核心内容是：The elves don’t have to be the only ones busy in the workshop this holiday season. With the lights twinkling and the gi…
  - 推荐理由：来自官方发布面，可信度比二手转述更高
  - 关键信号：信号来源：官方 RSS。
  - 原文摘要：The elves don’t have to be the only ones busy in the workshop this holiday season. With the lights twinkling and the gift wrap out, it’s the perfect time to give someone — or your…

- [NVIDIA and Microsoft Expand Accelerated Computing From Azure to Windows PCs](https://blogs.nvidia.com/blog/microsoft-ignite-accelerated-computing-azure-windows-pcs/)
  - 中文说明：主体：NVIDIA AI；事件类型：观察事项；来源：官方资讯源；评分：23.00；标签：基础设施。
  - 摘要：这是官方发布源中的一条更新，核心内容是：NVIDIA and Microsoft are extending their full-stack collaboration to help organizations build, customize and deploy int…
  - 推荐理由：来自官方发布面，可信度比二手转述更高
  - 关键信号：信号来源：官方 RSS；主题更偏案例/采用情况。
  - 原文摘要：NVIDIA and Microsoft are extending their full-stack collaboration to help organizations build, customize and deploy intelligent applications — from next-generation infrastructure…

- [Season’s Streamings and Savings: Black Friday Deals Come to GeForce NOW](https://blogs.nvidia.com/blog/geforce-now-thursday-black-friday-2026/)
  - 中文说明：主体：NVIDIA AI；事件类型：观察事项；来源：官方资讯源；评分：23.00；标签：未打标签。
  - 摘要：这是官方发布源中的一条更新，核心内容是：GeForce NOW is kicking off Black Friday with more reasons to make time for gaming. Six-month memberships are back for a…
  - 推荐理由：来自官方发布面，可信度比二手转述更高
  - 关键信号：信号来源：官方 RSS。
  - 原文摘要：GeForce NOW is kicking off Black Friday with more reasons to make time for gaming. Six-month memberships are back for a limited time. Save 30% on the first six-month term of a Per…

### Together AI（2 条重点）

- [Security event: Prompt leakage for requests in June and July of 2026](https://www.together.ai/blog/security-event-prompt-leakage-for-requests-in-june-and-july-of-2026)
  - 中文说明：主体：Together AI；事件类型：观察事项；来源：官方资讯源；评分：23.00；标签：基础设施。
  - 摘要：这是官方发布源中的一条更新，核心内容是：We are notifying customers about a security incident involving a subset of prompts submitted to Together AI’s serverles…
  - 推荐理由：来自官方发布面，可信度比二手转述更高
  - 关键信号：信号来源：官方 RSS；主题更偏案例/采用情况。
  - 原文摘要：We are notifying customers about a security incident involving a subset of prompts submitted to Together AI’s serverless inference service in June and July 2026.

- [Tencent Hy4 is live on Together AI](https://www.together.ai/blog/tencent-hy4)
  - 中文说明：主体：Together AI；事件类型：观察事项；来源：官方资讯源；评分：23.00；标签：编程、图像。
  - 摘要：这是官方发布源中的一条更新，核心内容是：Tencent Hy4 is live on Together AI. We tested its image input by extracting and rebuilding a chart, then tried its codi…
  - 推荐理由：来自官方发布面，可信度比二手转述更高
  - 关键信号：信号来源：官方 RSS。
  - 原文摘要：Tencent Hy4 is live on Together AI. We tested its image input by extracting and rebuilding a chart, then tried its coding with a browser game generated from one prompt.
