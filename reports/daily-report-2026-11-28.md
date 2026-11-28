# AI 情报雷达日报（2026-11-28）

当前展示池累计 241 条事件。日报已改成按厂商合并展示，并补充“摘要 / 推荐理由 / 关键信号”，帮助快速判断什么值得继续点开。

数据概况： 厂商新品 4 条； 新模型 121 条； 新开源项目 101 条； 其他观察 15 条。

## 厂商新品（4）

### Together AI（2 条重点）

- [Introducing preemptible compute: the same compute, half the price](https://www.together.ai/blog/introducing-preemptible-compute-the-same-compute-half-the-price)
  - 中文说明：主体：Together AI；事件类型：产品发布；来源：官方资讯源；评分：54.12；标签：未打标签。
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
  - 中文说明：主体：OpenAI；事件类型：产品发布；来源：官方资讯源；评分：51.45；标签：Agent。
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
  - 中文说明：主体：月之暗面；事件类型：模型发布；来源：Hugging Face 模型流；评分：92.63；标签：8-bit、编程、compressed-tensors、conversational、custom_code、endpoints_compatible、eval-results、图像、image-text-to-text、kimi_k31、license:other、region:us、safetensors、text-generation、transformers。
  - 摘要：`moonshotai/Kimi-K3.1-Pro` 的 Hugging Face 模型页最近发生了更新，通常对应新权重、量化版本、模型卡或可用性变化。 当前可见下载量约 111764，点赞约 2571。
  - 推荐理由：模型分发页显示下载量约 111764；社区点赞约 2571；这是模型层面的直接更新信号，不是二手媒体转述
  - 关键信号：标签：transformers / safetensors / kimi_k31 / text-generation / compressed-tensors / conversational；下载量：111764；点赞：2571；信号来源：Hugging Face 模型页
  - 原文摘要：tags=transformers, safetensors, kimi_k31, text-generation, compressed-tensors, conversational; downloads=111764; likes=2571

- [moonshotai/Kimi-K3 updated](https://huggingface.co/moonshotai/Kimi-K3)
  - 中文说明：主体：月之暗面；事件类型：模型发布；来源：Hugging Face 模型流；评分：89.46；标签：8-bit、编程、compressed-tensors、conversational、custom_code、deploy:sagemaker、eval-results、feature-extraction、图像、image-text-to-text、kimi_k3、license:other、region:us、safetensors、transformers。
  - 摘要：`moonshotai/Kimi-K3` 的 Hugging Face 模型页最近发生了更新，通常对应新权重、量化版本、模型卡或可用性变化。 当前可见下载量约 595480，点赞约 12034。
  - 推荐理由：模型分发页显示下载量约 595480；社区点赞约 12034；这是模型层面的直接更新信号，不是二手媒体转述
  - 关键信号：标签：transformers / safetensors / kimi_k3 / feature-extraction / compressed-tensors / conversational；下载量：595480；点赞：12034；信号来源：Hugging Face 模型页
  - 原文摘要：tags=transformers, safetensors, kimi_k3, feature-extraction, compressed-tensors, conversational; downloads=595480; likes=12034

- [moonshotai/Kimi-K2.5 updated](https://huggingface.co/moonshotai/Kimi-K2.5)
  - 中文说明：主体：月之暗面；事件类型：模型发布；来源：Hugging Face 模型流；评分：85.00；标签：arxiv:2602.02276、编程、compressed-tensors、conversational、custom_code、deploy:sagemaker、eval-results、feature-extraction、图像、image-text-to-text、kimi_k25、license:other、region:us、safetensors、transformers。
  - 摘要：`moonshotai/Kimi-K2.5` 的 Hugging Face 模型页最近发生了更新，通常对应新权重、量化版本、模型卡或可用性变化。 当前可见下载量约 280040，点赞约 2903。
  - 推荐理由：模型分发页显示下载量约 280040；社区点赞约 2903；这是模型层面的直接更新信号，不是二手媒体转述
  - 关键信号：标签：transformers / safetensors / kimi_k25 / feature-extraction / compressed-tensors / image-text-to-text；下载量：280040；点赞：2903；信号来源：Hugging Face 模型页
  - 原文摘要：tags=transformers, safetensors, kimi_k25, feature-extraction, compressed-tensors, image-text-to-text; downloads=280040; likes=2903

### MiniMax（3 条重点）

- [MiniMaxAI/MiniMax-H3 updated](https://huggingface.co/MiniMaxAI/MiniMax-H3)
  - 中文说明：主体：MiniMax；事件类型：模型发布；来源：Hugging Face 模型流；评分：88.94；标签：audio-to-audio-video、audio-video-generation、de、diffusers、en、es、fr、图像、image-text-to-audio-video、image-text-to-video、image-to-audio-video、image-to-video、license:other、minimax-h3、多模态、nl、reference-to-audio-video、region:us、safetensors、sv、synchronized-audio-video、text-to-audio-video、text-to-video、视频、video-to-audio-video、video-to-video、语音。
  - 摘要：`MiniMaxAI/MiniMax-H3` 的 Hugging Face 模型页最近发生了更新，通常对应新权重、量化版本、模型卡或可用性变化。 当前可见下载量约 5971579，点赞约 7447。
  - 推荐理由：模型分发页显示下载量约 5971579；社区点赞约 7447；这是模型层面的直接更新信号，不是二手媒体转述
  - 关键信号：标签：minimax-h3 / diffusers / safetensors / text-to-video / image-to-video / image-text-to-video；下载量：5971579；点赞：7447；信号来源：Hugging Face 模型页
  - 原文摘要：tags=minimax-h3, diffusers, safetensors, text-to-video, image-to-video, image-text-to-video; downloads=5971579; likes=7447

- [MiniMaxAI/MiniMax-M2 updated](https://huggingface.co/MiniMaxAI/MiniMax-M2)
  - 中文说明：主体：MiniMax；事件类型：模型发布；来源：Hugging Face 模型流；评分：85.00；标签：arxiv:2504.07164、arxiv:2509.06501、arxiv:2509.13160、编程、conversational、custom_code、deploy:azure、deploy:sagemaker、endpoints_compatible、eval-results、fp8、license:other、minimax_m2、region:us、safetensors、text-generation、transformers。
  - 摘要：`MiniMaxAI/MiniMax-M2` 的 Hugging Face 模型页最近发生了更新，通常对应新权重、量化版本、模型卡或可用性变化。 当前可见下载量约 109457，点赞约 1512。
  - 推荐理由：模型分发页显示下载量约 109457；社区点赞约 1512；这是模型层面的直接更新信号，不是二手媒体转述
  - 关键信号：标签：transformers / safetensors / minimax_m2 / text-generation / conversational / custom_code；下载量：109457；点赞：1512；信号来源：Hugging Face 模型页
  - 原文摘要：tags=transformers, safetensors, minimax_m2, text-generation, conversational, custom_code; downloads=109457; likes=1512

- [MiniMaxAI/MiniMax-M2.1 updated](https://huggingface.co/MiniMaxAI/MiniMax-M2.1)
  - 中文说明：主体：MiniMax；事件类型：模型发布；来源：Hugging Face 模型流；评分：85.00；标签：arxiv:2509.06501、编程、conversational、custom_code、deploy:azure、deploy:sagemaker、endpoints_compatible、eval-results、fp8、license:other、minimax_m2、region:us、safetensors、text-generation、transformers。
  - 摘要：`MiniMaxAI/MiniMax-M2.1` 的 Hugging Face 模型页最近发生了更新，通常对应新权重、量化版本、模型卡或可用性变化。 当前可见下载量约 12851，点赞约 1372。
  - 推荐理由：模型分发页显示下载量约 12851；社区点赞约 1372；这是模型层面的直接更新信号，不是二手媒体转述
  - 关键信号：标签：transformers / safetensors / minimax_m2 / text-generation / conversational / custom_code；下载量：12851；点赞：1372；信号来源：Hugging Face 模型页
  - 原文摘要：tags=transformers, safetensors, minimax_m2, text-generation, conversational, custom_code; downloads=12851; likes=1372

### Qwen（3 条重点）

- [Qwen/Qwen2-VL-2B-Instruct updated](https://huggingface.co/Qwen/Qwen2-VL-2B-Instruct)
  - 中文说明：主体：Qwen；事件类型：模型发布；来源：Hugging Face 模型流；评分：85.00；标签：arxiv:2308.12966、arxiv:2409.12191、base_model:Qwen/Qwen2-VL-2B、base_model:finetune:Qwen/Qwen2-VL-2B、conversational、deploy:azure、en、endpoints_compatible、图像、image-text-to-text、基础设施、license:apache-2.0、多模态、qwen2_vl、region:us、safetensors、text-generation-inference、transformers。
  - 摘要：`Qwen/Qwen2-VL-2B-Instruct` 的 Hugging Face 模型页最近发生了更新，通常对应新权重、量化版本、模型卡或可用性变化。 当前可见下载量约 904819，点赞约 534。
  - 推荐理由：模型分发页显示下载量约 904819；社区点赞约 534；这是模型层面的直接更新信号，不是二手媒体转述
  - 关键信号：标签：transformers / safetensors / qwen2_vl / image-text-to-text / multimodal / conversational；下载量：904819；点赞：534；信号来源：Hugging Face 模型页
  - 原文摘要：tags=transformers, safetensors, qwen2_vl, image-text-to-text, multimodal, conversational; downloads=904819; likes=534

- [Qwen/Qwen3.6-27B updated](https://huggingface.co/Qwen/Qwen3.6-27B)
  - 中文说明：主体：Qwen；事件类型：模型发布；来源：Hugging Face 模型流；评分：85.00；标签：conversational、deploy:azure、deploy:sagemaker、endpoints_compatible、eval-results、图像、image-text-to-text、license:apache-2.0、qwen3_5、region:us、safetensors、transformers。
  - 摘要：`Qwen/Qwen3.6-27B` 的 Hugging Face 模型页最近发生了更新，通常对应新权重、量化版本、模型卡或可用性变化。 当前可见下载量约 2235019，点赞约 2366。
  - 推荐理由：模型分发页显示下载量约 2235019；社区点赞约 2366；这是模型层面的直接更新信号，不是二手媒体转述
  - 关键信号：标签：transformers / safetensors / qwen3_5 / image-text-to-text / conversational / license:apache-2.0；下载量：2235019；点赞：2366；信号来源：Hugging Face 模型页
  - 原文摘要：tags=transformers, safetensors, qwen3_5, image-text-to-text, conversational, license:apache-2.0; downloads=2235019; likes=2366

- [Qwen/Qwen3.5-27B updated](https://huggingface.co/Qwen/Qwen3.5-27B)
  - 中文说明：主体：Qwen；事件类型：模型发布；来源：Hugging Face 模型流；评分：85.00；标签：conversational、deploy:azure、deploy:sagemaker、endpoints_compatible、eval-results、图像、image-text-to-text、license:apache-2.0、qwen3_5、region:us、safetensors、transformers。
  - 摘要：`Qwen/Qwen3.5-27B` 的 Hugging Face 模型页最近发生了更新，通常对应新权重、量化版本、模型卡或可用性变化。 当前可见下载量约 1381464，点赞约 1099。
  - 推荐理由：模型分发页显示下载量约 1381464；社区点赞约 1099；这是模型层面的直接更新信号，不是二手媒体转述
  - 关键信号：标签：transformers / safetensors / qwen3_5 / image-text-to-text / conversational / license:apache-2.0；下载量：1381464；点赞：1099；信号来源：Hugging Face 模型页
  - 原文摘要：tags=transformers, safetensors, qwen3_5, image-text-to-text, conversational, license:apache-2.0; downloads=1381464; likes=1099

### DeepSeek（3 条重点）

- [deepseek-ai/DeepSeek-V4.1-Flash-1017 updated](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)
  - 中文说明：主体：DeepSeek；事件类型：模型发布；来源：Hugging Face 模型流；评分：85.00；标签：8-bit、conversational、deepseek_v41、deploy:azure、endpoints_compatible、eval-results、fp8、图像、image-text-to-text、license:mit、region:us、safetensors、text-generation、transformers。
  - 摘要：`deepseek-ai/DeepSeek-V4.1-Flash-1017` 的 Hugging Face 模型页最近发生了更新，通常对应新权重、量化版本、模型卡或可用性变化。 当前可见下载量约 552671，点赞约 6819。
  - 推荐理由：模型分发页显示下载量约 552671；社区点赞约 6819；这是模型层面的直接更新信号，不是二手媒体转述
  - 关键信号：标签：transformers / safetensors / deepseek_v41 / text-generation / image-text-to-text / conversational；下载量：552671；点赞：6819；信号来源：Hugging Face 模型页
  - 原文摘要：tags=transformers, safetensors, deepseek_v41, text-generation, image-text-to-text, conversational; downloads=552671; likes=6819

- [deepseek-ai/DeepSeek-V4.1-Flash updated](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
  - 中文说明：主体：DeepSeek；事件类型：模型发布；来源：Hugging Face 模型流；评分：85.00；标签：8-bit、conversational、deepseek_v41、deploy:azure、deploy:sagemaker、endpoints_compatible、eval-results、fp8、图像、image-text-to-text、license:mit、region:us、safetensors、text-generation、transformers。
  - 摘要：`deepseek-ai/DeepSeek-V4.1-Flash` 的 Hugging Face 模型页最近发生了更新，通常对应新权重、量化版本、模型卡或可用性变化。 当前可见下载量约 957631，点赞约 5124。
  - 推荐理由：模型分发页显示下载量约 957631；社区点赞约 5124；这是模型层面的直接更新信号，不是二手媒体转述
  - 关键信号：标签：transformers / safetensors / deepseek_v41 / text-generation / image-text-to-text / conversational；下载量：957631；点赞：5124；信号来源：Hugging Face 模型页
  - 原文摘要：tags=transformers, safetensors, deepseek_v41, text-generation, image-text-to-text, conversational; downloads=957631; likes=5124

- [deepseek-ai/DeepSeek-V4-Flash-Vision-Exp updated](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp)
  - 中文说明：主体：DeepSeek；事件类型：模型发布；来源：Hugging Face 模型流；评分：85.00；标签：8-bit、deepseek_v4、endpoints_compatible、eval-results、fp8、图像、image-text-to-text、license:mit、region:us、safetensors、text-generation、transformers。
  - 摘要：`deepseek-ai/DeepSeek-V4-Flash-Vision-Exp` 的 Hugging Face 模型页最近发生了更新，通常对应新权重、量化版本、模型卡或可用性变化。 当前可见下载量约 28005，点赞约 972。
  - 推荐理由：模型分发页显示下载量约 28005；社区点赞约 972；这是模型层面的直接更新信号，不是二手媒体转述
  - 关键信号：标签：transformers / safetensors / deepseek_v4 / text-generation / image-text-to-text / license:mit；下载量：28005；点赞：972；信号来源：Hugging Face 模型页
  - 原文摘要：tags=transformers, safetensors, deepseek_v4, text-generation, image-text-to-text, license:mit; downloads=28005; likes=972

### Zhipu AI（3 条重点）

- [zai-org/GLM-5.3-Flash updated](https://huggingface.co/zai-org/GLM-5.3-Flash)
  - 中文说明：主体：Zhipu AI；事件类型：模型发布；来源：Hugging Face 模型流；评分：85.00；标签：arxiv:2602.15763、conversational、deploy:azure、deploy:sagemaker、en、endpoints_compatible、eval-results、fp8、glm5_next、图像、image-text-to-text、license:mit、region:us、safetensors、transformers、zh。
  - 摘要：`zai-org/GLM-5.3-Flash` 的 Hugging Face 模型页最近发生了更新，通常对应新权重、量化版本、模型卡或可用性变化。 当前可见下载量约 6054355，点赞约 3365。
  - 推荐理由：模型分发页显示下载量约 6054355；社区点赞约 3365；这是模型层面的直接更新信号，不是二手媒体转述
  - 关键信号：标签：transformers / safetensors / glm5_next / image-text-to-text / conversational / en；下载量：6054355；点赞：3365；信号来源：Hugging Face 模型页
  - 原文摘要：tags=transformers, safetensors, glm5_next, image-text-to-text, conversational, en; downloads=6054355; likes=3365

- [zai-org/GLM-5.3 updated](https://huggingface.co/zai-org/GLM-5.3)
  - 中文说明：主体：Zhipu AI；事件类型：模型发布；来源：Hugging Face 模型流；评分：85.00；标签：arxiv:2602.15763、conversational、deploy:sagemaker、en、endpoints_compatible、eval-results、fp8、glm_moe_dsa、license:other、region:us、safetensors、text-generation、transformers、zh。
  - 摘要：`zai-org/GLM-5.3` 的 Hugging Face 模型页最近发生了更新，通常对应新权重、量化版本、模型卡或可用性变化。 当前可见下载量约 862778，点赞约 2574。
  - 推荐理由：模型分发页显示下载量约 862778；社区点赞约 2574；这是模型层面的直接更新信号，不是二手媒体转述
  - 关键信号：标签：transformers / safetensors / glm_moe_dsa / text-generation / conversational / en；下载量：862778；点赞：2574；信号来源：Hugging Face 模型页
  - 原文摘要：tags=transformers, safetensors, glm_moe_dsa, text-generation, conversational, en; downloads=862778; likes=2574

- [zai-org/GLM-OCR updated](https://huggingface.co/zai-org/GLM-OCR)
  - 中文说明：主体：Zhipu AI；事件类型：模型发布；来源：Hugging Face 模型流；评分：85.00；标签：arxiv:2603.10910、conversational、de、deploy:azure、deploy:sagemaker、en、endpoints_compatible、es、eval-results、fr、glm_ocr、图像、image-text-to-text、image-to-text、ja、ko、license:mit、region:us、ru、safetensors、transformers、zh。
  - 摘要：`zai-org/GLM-OCR` 的 Hugging Face 模型页最近发生了更新，通常对应新权重、量化版本、模型卡或可用性变化。 当前可见下载量约 2300173，点赞约 2249。
  - 推荐理由：模型分发页显示下载量约 2300173；社区点赞约 2249；这是模型层面的直接更新信号，不是二手媒体转述
  - 关键信号：标签：transformers / safetensors / glm_ocr / image-text-to-text / conversational / image-to-text；下载量：2300173；点赞：2249；信号来源：Hugging Face 模型页
  - 原文摘要：tags=transformers, safetensors, glm_ocr, image-text-to-text, conversational, image-to-text; downloads=2300173; likes=2249

### StepFun（3 条重点）

- [stepfun-ai/Step-3.7-Flash updated](https://huggingface.co/stepfun-ai/Step-3.7-Flash)
  - 中文说明：主体：StepFun；事件类型：模型发布；来源：Hugging Face 模型流；评分：85.00；标签：编程、conversational、custom_code、en、endpoints_compatible、eval-results、图像、image-text-to-text、license:apache-2.0、moe、多模态、region:us、safetensors、step3p7、transformers、vision-language。
  - 摘要：`stepfun-ai/Step-3.7-Flash` 的 Hugging Face 模型页最近发生了更新，通常对应新权重、量化版本、模型卡或可用性变化。 当前可见下载量约 11183，点赞约 465。
  - 推荐理由：模型分发页显示下载量约 11183；社区点赞约 465；这是模型层面的直接更新信号，不是二手媒体转述
  - 关键信号：标签：transformers / safetensors / step3p7 / image-text-to-text / vision-language / multimodal；下载量：11183；点赞：465；信号来源：Hugging Face 模型页
  - 原文摘要：tags=transformers, safetensors, step3p7, image-text-to-text, vision-language, multimodal; downloads=11183; likes=465

- [stepfun-ai/Step-3.5-Flash updated](https://huggingface.co/stepfun-ai/Step-3.5-Flash)
  - 中文说明：主体：StepFun；事件类型：模型发布；来源：Hugging Face 模型流；评分：85.00；标签：arxiv:2507.19427、arxiv:2601.05593、arxiv:2602.10604、编程、conversational、custom_code、eval-results、license:apache-2.0、region:us、safetensors、step3p5、text-generation、transformers。
  - 摘要：`stepfun-ai/Step-3.5-Flash` 的 Hugging Face 模型页最近发生了更新，通常对应新权重、量化版本、模型卡或可用性变化。 当前可见下载量约 158989，点赞约 846。
  - 推荐理由：模型分发页显示下载量约 158989；社区点赞约 846；这是模型层面的直接更新信号，不是二手媒体转述
  - 关键信号：标签：transformers / safetensors / step3p5 / text-generation / conversational / custom_code；下载量：158989；点赞：846；信号来源：Hugging Face 模型页
  - 原文摘要：tags=transformers, safetensors, step3p5, text-generation, conversational, custom_code; downloads=158989; likes=846

- [stepfun-ai/Step-3.7-Flash-GGUF updated](https://huggingface.co/stepfun-ai/Step-3.7-Flash-GGUF)
  - 中文说明：主体：StepFun；事件类型：模型发布；来源：Hugging Face 模型流；评分：73.90；标签：Agent、ar、base_model:quantized:stepfun-ai/Step-3.7-Flash、base_model:stepfun-ai/Step-3.7-Flash、conversational、de、en、endpoints_compatible、es、fr、gguf、hi、图像、image-text-to-text、imatrix、ja、ko、license:apache-2.0、llama.cpp、moe、多模态、quantized、推理、region:us、ru、tool-calling、vision、zh。
  - 摘要：`stepfun-ai/Step-3.7-Flash-GGUF` 的 Hugging Face 模型页最近发生了更新，通常对应新权重、量化版本、模型卡或可用性变化。 当前可见下载量约 2432，点赞约 178。
  - 推荐理由：模型分发页显示下载量约 2432；社区点赞约 178；这是模型层面的直接更新信号，不是二手媒体转述
  - 关键信号：标签：gguf / llama.cpp / quantized / imatrix / moe / agent；下载量：2432；点赞：178；信号来源：Hugging Face 模型页
  - 原文摘要：tags=gguf, llama.cpp, quantized, imatrix, moe, agent; downloads=2432; likes=178

## 新开源项目（101）

### Red2076-arch（1 条重点）

- [Red2076-arch/waifu2x-image-upscaler-windows is trending](https://github.com/Red2076-arch/waifu2x-image-upscaler-windows)
  - 中文说明：主体：Red2076-arch；事件类型：开源项目发布；来源：GitHub 发现流；评分：76.00；标签：图像。
  - 摘要：`Red2076-arch/waifu2x-image-upscaler-windows` 最近进入 GitHub 高活跃区间，属于面向 AI 应用或基础设施的开源项目。Free AI image upscaler and photo denoiser for Windows powered by Vulkan GPU acceleration and ncnn neural networks.
  - 推荐理由：当前 GitHub stars 约 776，说明已经形成一定关注度；近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度；属于近 24 小时内的新鲜动态
  - 关键信号：开源类型：面向 AI 应用或基础设施的开源项目；GitHub stars：776；信号来源：GitHub 发现流。
  - 原文摘要：Free AI image upscaler and photo denoiser for Windows powered by Vulkan GPU acceleration and ncnn neural networks.

### DeepSeek（3 条重点）

- [deepseek-ai/DeepJIT is trending](https://github.com/deepseek-ai/DeepJIT)
  - 中文说明：主体：DeepSeek；事件类型：开源项目发布；来源：GitHub 发现流；评分：75.92；标签：未打标签。
  - 摘要：`deepseek-ai/DeepJIT` 最近进入 GitHub 高活跃区间，属于面向 AI 应用或基础设施的开源项目。A lightweight library for xPU kernel JIT compilation
  - 推荐理由：近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度；属于近 24 小时内的新鲜动态
  - 关键信号：开源类型：面向 AI 应用或基础设施的开源项目；GitHub stars：480；信号来源：GitHub 发现流。
  - 原文摘要：A lightweight library for xPU kernel JIT compilation

- [deepseek-ai/DeepEP is trending](https://github.com/deepseek-ai/DeepEP)
  - 中文说明：主体：DeepSeek；事件类型：开源项目发布；来源：GitHub 发现流；评分：75.92；标签：未打标签。
  - 摘要：`deepseek-ai/DeepEP` 最近进入 GitHub 高活跃区间，属于面向 AI 应用或基础设施的开源项目。DeepEP: an efficient expert-parallel communication library
  - 推荐理由：当前 GitHub stars 约 10480，已不是早期小项目；近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度；属于近 24 小时内的新鲜动态
  - 关键信号：开源类型：面向 AI 应用或基础设施的开源项目；GitHub stars：10480；信号来源：GitHub 发现流。
  - 原文摘要：DeepEP: an efficient expert-parallel communication library

- [deepseek-ai/TileKernels is trending](https://github.com/deepseek-ai/TileKernels)
  - 中文说明：主体：DeepSeek；事件类型：开源项目发布；来源：GitHub 发现流；评分：75.92；标签：未打标签。
  - 摘要：`deepseek-ai/TileKernels` 最近进入 GitHub 高活跃区间，属于面向 AI 应用或基础设施的开源项目。A kernel library written in tilelang
  - 推荐理由：当前 GitHub stars 约 2091，说明已经形成一定关注度；近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度；属于近 24 小时内的新鲜动态
  - 关键信号：开源类型：面向 AI 应用或基础设施的开源项目；GitHub stars：2091；信号来源：GitHub 发现流。
  - 原文摘要：A kernel library written in tilelang

### Qwen（3 条重点）

- [QwenLM/qwen-code is trending](https://github.com/QwenLM/qwen-code)
  - 中文说明：主体：Qwen；事件类型：开源项目发布；来源：GitHub 发现流；评分：75.92；标签：Agent、编程。
  - 摘要：`QwenLM/qwen-code` 最近进入 GitHub 高活跃区间，属于面向 AI agent 或编码助手的开源项目。An open-source AI coding agent that lives in your terminal.
  - 推荐理由：当前 GitHub stars 约 30992，已不是早期小项目；近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度；属于近 24 小时内的新鲜动态
  - 关键信号：开源类型：面向 AI agent 或编码助手的开源项目；GitHub stars：30992；信号来源：GitHub 发现流。
  - 原文摘要：An open-source AI coding agent that lives in your terminal.

- [QwenLM/FlashQLA is trending](https://github.com/QwenLM/FlashQLA)
  - 中文说明：主体：Qwen；事件类型：开源项目发布；来源：GitHub 发现流；评分：74.04；标签：未打标签。
  - 摘要：`QwenLM/FlashQLA` 最近进入 GitHub 高活跃区间，属于面向 AI 应用或基础设施的开源项目。high-performance linear attention kernel library built on TileLang
  - 推荐理由：当前 GitHub stars 约 776，说明已经形成一定关注度；近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度；属于近 24 小时内的新鲜动态
  - 关键信号：开源类型：面向 AI 应用或基础设施的开源项目；GitHub stars：776；信号来源：GitHub 发现流。
  - 原文摘要：high-performance linear attention kernel library built on TileLang

- [QwenLM/Qwen-MM-Plugins is trending](https://github.com/QwenLM/Qwen-MM-Plugins)
  - 中文说明：主体：Qwen；事件类型：开源项目发布；来源：GitHub 发现流；评分：72.98；标签：Agent、多模态。
  - 摘要：`QwenLM/Qwen-MM-Plugins` 最近进入 GitHub 高活跃区间，属于面向 AI agent 或编码助手的开源项目。Make any agent harness multimodal-native.
  - 推荐理由：当前 GitHub stars 约 3216，说明已经形成一定关注度；近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度；属于近 24 小时内的新鲜动态
  - 关键信号：开源类型：面向 AI agent 或编码助手的开源项目；GitHub stars：3216；信号来源：GitHub 发现流。
  - 原文摘要：Make any agent harness multimodal-native.

### ModelScope（3 条重点）

- [modelscope/ms-swift is trending](https://github.com/modelscope/ms-swift)
  - 中文说明：主体：ModelScope；事件类型：开源项目发布；来源：GitHub 发现流；评分：75.76；标签：未打标签。
  - 摘要：`modelscope/ms-swift` 最近进入 GitHub 高活跃区间，属于围绕模型权重、模型推理或模型家族的开源项目。Use PEFT or Full-parameter to CPT/SFT/DPO/GRPO 600+ LLMs (Qwen3.8, DeepSeek-V4, GLM-5.1, InternLM3, Llama4, ...) and 30…
  - 推荐理由：当前 GitHub stars 约 16188，已不是早期小项目；近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度；属于近 24 小时内的新鲜动态
  - 关键信号：开源类型：围绕模型权重、模型推理或模型家族的开源项目；GitHub stars：16188；信号来源：GitHub 发现流。
  - 原文摘要：Use PEFT or Full-parameter to CPT/SFT/DPO/GRPO 600+ LLMs (Qwen3.8, DeepSeek-V4, GLM-5.1, InternLM3, Llama4, ...) and 300+ MLLMs (Qwen3-VL, Qwen3-Omni, InternVL3.5, Ovis2.5, GLM5.3…

- [modelscope/DiffSynth-Studio is trending](https://github.com/modelscope/DiffSynth-Studio)
  - 中文说明：主体：ModelScope；事件类型：开源项目发布；来源：GitHub 发现流；评分：75.65；标签：图像。
  - 摘要：`modelscope/DiffSynth-Studio` 最近进入 GitHub 高活跃区间，属于围绕模型权重、模型推理或模型家族的开源项目。Enjoy the magic of Diffusion models!
  - 推荐理由：当前 GitHub stars 约 13448，已不是早期小项目；近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度；属于近 24 小时内的新鲜动态
  - 关键信号：开源类型：围绕模型权重、模型推理或模型家族的开源项目；GitHub stars：13448；信号来源：GitHub 发现流。
  - 原文摘要：Enjoy the magic of Diffusion models!

- [modelscope/evalscope is trending](https://github.com/modelscope/evalscope)
  - 中文说明：主体：ModelScope；事件类型：开源项目发布；来源：GitHub 发现流；评分：75.64；标签：未打标签。
  - 摘要：`modelscope/evalscope` 最近进入 GitHub 高活跃区间，属于用于评测模型或 agent 能力的开源项目。A streamlined and customizable framework for efficient large model (LLM, VLM, AIGC) evaluation and performance benchmar…
  - 推荐理由：当前 GitHub stars 约 3744，说明已经形成一定关注度；近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度；属于近 24 小时内的新鲜动态
  - 关键信号：开源类型：用于评测模型或 agent 能力的开源项目；GitHub stars：3744；信号来源：GitHub 发现流。
  - 原文摘要：A streamlined and customizable framework for efficient large model (LLM, VLM, AIGC) evaluation and performance benchmarking.

### 月之暗面（3 条重点）

- [MoonshotAI/kimi-code is trending](https://github.com/MoonshotAI/kimi-code)
  - 中文说明：主体：月之暗面；事件类型：开源项目发布；来源：GitHub 发现流；评分：75.72；标签：Agent、编程。
  - 摘要：`MoonshotAI/kimi-code` 最近进入 GitHub 高活跃区间，属于面向 AI agent 或编码助手的开源项目。Kimi Code CLI — The Starting Point for Next-Gen Agents
  - 推荐理由：当前 GitHub stars 约 8318，已不是早期小项目；近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度；属于近 24 小时内的新鲜动态
  - 关键信号：开源类型：面向 AI agent 或编码助手的开源项目；GitHub stars：8318；信号来源：GitHub 发现流。
  - 原文摘要：Kimi Code CLI — The Starting Point for Next-Gen Agents

- [MoonshotAI/FlashKDA is trending](https://github.com/MoonshotAI/FlashKDA)
  - 中文说明：主体：月之暗面；事件类型：开源项目发布；来源：GitHub 发现流；评分：70.05；标签：未打标签。
  - 摘要：`MoonshotAI/FlashKDA` 最近进入 GitHub 高活跃区间，属于面向 AI 应用或基础设施的开源项目。FlashKDA: high-performance Kimi Delta Attention kernels
  - 推荐理由：当前 GitHub stars 约 1304，说明已经形成一定关注度；近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度
  - 关键信号：开源类型：面向 AI 应用或基础设施的开源项目；GitHub stars：1304；信号来源：GitHub 发现流。
  - 原文摘要：FlashKDA: high-performance Kimi Delta Attention kernels

- [MoonshotAI/MoonEP is trending](https://github.com/MoonshotAI/MoonEP)
  - 中文说明：主体：月之暗面；事件类型：开源项目发布；来源：GitHub 发现流；评分：65.66；标签：未打标签。
  - 摘要：`MoonshotAI/MoonEP` 最近进入 GitHub 高活跃区间，属于面向 AI 应用或基础设施的开源项目。MoonEP: A Perfectly Balanced Expert Parallelism Library via Dynamic Redundant Experts
  - 推荐理由：当前 GitHub stars 约 1220，说明已经形成一定关注度；近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度
  - 关键信号：开源类型：面向 AI 应用或基础设施的开源项目；GitHub stars：1220；信号来源：GitHub 发现流。
  - 原文摘要：MoonEP: A Perfectly Balanced Expert Parallelism Library via Dynamic Redundant Experts

### MiniMax（3 条重点）

- [MiniMax-AI/minimax-code is trending](https://github.com/MiniMax-AI/minimax-code)
  - 中文说明：主体：MiniMax；事件类型：开源项目发布；来源：GitHub 发现流；评分：75.62；标签：Agent、编程。
  - 摘要：`MiniMax-AI/minimax-code` 最近进入 GitHub 高活跃区间，属于面向 AI agent 或编码助手的开源项目。An open-source coding agent for your terminal, powered by MiniMax.
  - 推荐理由：当前 GitHub stars 约 2299，说明已经形成一定关注度；近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度；属于近 24 小时内的新鲜动态
  - 关键信号：开源类型：面向 AI agent 或编码助手的开源项目；GitHub stars：2299；信号来源：GitHub 发现流。
  - 原文摘要：An open-source coding agent for your terminal, powered by MiniMax.

- [MiniMax-AI/MSA is trending](https://github.com/MiniMax-AI/MSA)
  - 中文说明：主体：MiniMax；事件类型：开源项目发布；来源：GitHub 发现流；评分：70.38；标签：未打标签。
  - 摘要：`MiniMax-AI/MSA` 最近进入 GitHub 高活跃区间，属于面向 AI 应用或基础设施的开源项目。当前公开描述较少。
  - 推荐理由：近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度
  - 关键信号：开源类型：面向 AI 应用或基础设施的开源项目；GitHub stars：441；信号来源：GitHub 发现流。

- [MiniMax-AI/OpenAgentCore is trending](https://github.com/MiniMax-AI/OpenAgentCore)
  - 中文说明：主体：MiniMax；事件类型：开源项目发布；来源：GitHub 发现流；评分：66.78；标签：Agent、编程、基础设施。
  - 摘要：`MiniMax-AI/OpenAgentCore` 最近进入 GitHub 高活跃区间，属于面向 AI agent 或编码助手的开源项目。The OpenAI Agents API, open source and self-hosted. Run Codex, Claude Code or MiniMax Code on your own machines with yo…
  - 推荐理由：近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度
  - 关键信号：开源类型：面向 AI agent 或编码助手的开源项目；GitHub stars：354；信号来源：GitHub 发现流。
  - 原文摘要：The OpenAI Agents API, open source and self-hosted. Run Codex, Claude Code or MiniMax Code on your own machines with your own models, through the official OpenAI SDK.

### ByteDance Seed（3 条重点）

- [ByteDance-Seed/VeOmni is trending](https://github.com/ByteDance-Seed/VeOmni)
  - 中文说明：主体：ByteDance Seed；事件类型：开源项目发布；来源：GitHub 发现流；评分：75.52；标签：未打标签。
  - 摘要：`ByteDance-Seed/VeOmni` 最近进入 GitHub 高活跃区间，属于围绕模型权重、模型推理或模型家族的开源项目。VeOmni: Scaling Any Modality Model Training with Model-Centric Distributed Recipe Zoo
  - 推荐理由：当前 GitHub stars 约 2309，说明已经形成一定关注度；近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度；属于近 24 小时内的新鲜动态
  - 关键信号：开源类型：围绕模型权重、模型推理或模型家族的开源项目；GitHub stars：2309；信号来源：GitHub 发现流。
  - 原文摘要：VeOmni: Scaling Any Modality Model Training with Model-Centric Distributed Recipe Zoo

- [ByteDance-Seed/EdgeBench is trending](https://github.com/ByteDance-Seed/EdgeBench)
  - 中文说明：主体：ByteDance Seed；事件类型：开源项目发布；来源：GitHub 发现流；评分：72.40；标签：未打标签。
  - 摘要：`ByteDance-Seed/EdgeBench` 最近进入 GitHub 高活跃区间，属于面向 AI 应用或基础设施的开源项目。EdgeBench: Unveiling scaling laws of learning from real-world environments
  - 推荐理由：近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度；属于近 24 小时内的新鲜动态
  - 关键信号：开源类型：面向 AI 应用或基础设施的开源项目；GitHub stars：487；信号来源：GitHub 发现流。
  - 原文摘要：EdgeBench: Unveiling scaling laws of learning from real-world environments

- [ByteDance-Seed/Triton-distributed is trending](https://github.com/ByteDance-Seed/Triton-distributed)
  - 中文说明：主体：ByteDance Seed；事件类型：开源项目发布；来源：GitHub 发现流；评分：71.56；标签：未打标签。
  - 摘要：`ByteDance-Seed/Triton-distributed` 最近进入 GitHub 高活跃区间，属于面向 AI 应用或基础设施的开源项目。Distributed Compiler and Optimized Parallel Kernels
  - 推荐理由：当前 GitHub stars 约 1595，说明已经形成一定关注度；近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度
  - 关键信号：开源类型：面向 AI 应用或基础设施的开源项目；GitHub stars：1595；信号来源：GitHub 发现流。
  - 原文摘要：Distributed Compiler and Optimized Parallel Kernels

### OpenAI（3 条重点）

- [openai/openai-python: v3.60.0](https://github.com/openai/openai-python/releases/tag/v3.60.0)
  - 中文说明：主体：OpenAI；事件类型：开源项目发布；来源：GitHub Release；评分：73.31；标签：语音、基础设施。
  - 摘要：`openai/openai-python` 刚发布了一个新版本，说明这个 SDK 或开源项目最近有明确的版本更新。
  - 推荐理由：release 代表项目维护者已经给出明确版本边界，信号强于普通提交
  - 关键信号：信号来源：GitHub Release；适合优先查看 release notes、破坏性变更和版本号。
  - 原文摘要：## [3.60.0](https://github.com/openai/openai-python/compare/v3.59.0...v3.60.0) (2026-11-26) ### Features * **api:** add spend alerts and response compaction fields ([#4335](https:…

- [openai/openai-python: v3.59.0](https://github.com/openai/openai-python/releases/tag/v3.59.0)
  - 中文说明：主体：OpenAI；事件类型：开源项目发布；来源：GitHub Release；评分：67.34；标签：Agent、基础设施。
  - 摘要：`openai/openai-python` 刚发布了一个新版本，说明这个 SDK 或开源项目最近有明确的版本更新。
  - 推荐理由：release 代表项目维护者已经给出明确版本边界，信号强于普通提交
  - 关键信号：信号来源：GitHub Release；适合优先查看 release notes、破坏性变更和版本号。
  - 原文摘要：## [3.59.0](https://github.com/openai/openai-python/compare/v3.58.0...v3.59.0) (2026-11-24) ### Features * **api:** add healthcare model IDs for Responses ([#4327](https://github.…

- [openai/openai-python: v3.58.0](https://github.com/openai/openai-python/releases/tag/v3.58.0)
  - 中文说明：主体：OpenAI；事件类型：开源项目发布；来源：GitHub Release；评分：63.29；标签：Agent、基础设施。
  - 摘要：`openai/openai-python` 刚发布了一个新版本，说明这个 SDK 或开源项目最近有明确的版本更新。
  - 推荐理由：release 代表项目维护者已经给出明确版本边界，信号强于普通提交
  - 关键信号：信号来源：GitHub Release；适合优先查看 release notes、破坏性变更和版本号。
  - 原文摘要：## [3.58.0](https://github.com/openai/openai-python/compare/v3.57.0...v3.58.0) (2026-11-23) ### Features * **api:** set and read agent session spending limits ([#4315](https://git…

### Tencent Hunyuan（3 条重点）

- [Tencent-Hunyuan/HunyuanWorld-Mirror is trending](https://github.com/Tencent-Hunyuan/HunyuanWorld-Mirror)
  - 中文说明：主体：Tencent Hunyuan；事件类型：开源项目发布；来源：GitHub 发现流；评分：72.78；标签：未打标签。
  - 摘要：`Tencent-Hunyuan/HunyuanWorld-Mirror` 最近进入 GitHub 高活跃区间，属于围绕模型权重、模型推理或模型家族的开源项目。[ICML 2026] WorldMirror: Fast and Universal 3D reconstruction model for versatile tasks
  - 推荐理由：当前 GitHub stars 约 1236，说明已经形成一定关注度；近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度；属于近 24 小时内的新鲜动态
  - 关键信号：开源类型：围绕模型权重、模型推理或模型家族的开源项目；GitHub stars：1236；信号来源：GitHub 发现流。
  - 原文摘要：[ICML 2026] WorldMirror: Fast and Universal 3D reconstruction model for versatile tasks

- [Tencent-Hunyuan/UniRL is trending](https://github.com/Tencent-Hunyuan/UniRL)
  - 中文说明：主体：Tencent Hunyuan；事件类型：开源项目发布；来源：GitHub 发现流；评分：71.84；标签：多模态。
  - 摘要：`Tencent-Hunyuan/UniRL` 最近进入 GitHub 高活跃区间，属于围绕模型权重、模型推理或模型家族的开源项目。UniRL is a Framework for Unified Multimodal Model Reinforcement Learning
  - 推荐理由：当前 GitHub stars 约 1052，说明已经形成一定关注度；近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度
  - 关键信号：开源类型：围绕模型权重、模型推理或模型家族的开源项目；GitHub stars：1052；信号来源：GitHub 发现流。
  - 原文摘要：UniRL is a Framework for Unified Multimodal Model Reinforcement Learning

- [Tencent-Hunyuan/HunyuanWorld-Voyager is trending](https://github.com/Tencent-Hunyuan/HunyuanWorld-Voyager)
  - 中文说明：主体：Tencent Hunyuan；事件类型：开源项目发布；来源：GitHub 发现流；评分：68.51；标签：视频。
  - 摘要：`Tencent-Hunyuan/HunyuanWorld-Voyager` 最近进入 GitHub 高活跃区间，属于围绕模型权重、模型推理或模型家族的开源项目。Voyager is an interactive RGBD video generation model conditioned on camera input, and supports real-time 3D reconstruc…
  - 推荐理由：当前 GitHub stars 约 1613，说明已经形成一定关注度；近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度
  - 关键信号：开源类型：围绕模型权重、模型推理或模型家族的开源项目；GitHub stars：1613；信号来源：GitHub 发现流。
  - 原文摘要：Voyager is an interactive RGBD video generation model conditioned on camera input, and supports real-time 3D reconstruction.

### InternLM（3 条重点）

- [InternLM/lmdeploy is trending](https://github.com/InternLM/lmdeploy)
  - 中文说明：主体：InternLM；事件类型：开源项目发布；来源：GitHub 发现流；评分：72.46；标签：未打标签。
  - 摘要：`InternLM/lmdeploy` 最近进入 GitHub 高活跃区间，属于围绕模型权重、模型推理或模型家族的开源项目。LMDeploy is a toolkit for compressing, deploying, and serving LLMs.
  - 推荐理由：当前 GitHub stars 约 8157，已不是早期小项目；近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度；属于近 24 小时内的新鲜动态
  - 关键信号：开源类型：围绕模型权重、模型推理或模型家族的开源项目；GitHub stars：8157；信号来源：GitHub 发现流。
  - 原文摘要：LMDeploy is a toolkit for compressing, deploying, and serving LLMs.

- [InternLM/WildClawBench is trending](https://github.com/InternLM/WildClawBench)
  - 中文说明：主体：InternLM；事件类型：开源项目发布；来源：GitHub 发现流；评分：72.30；标签：Agent。
  - 摘要：`InternLM/WildClawBench` 最近进入 GitHub 高活跃区间，属于面向 AI agent 或编码助手的开源项目。An in-the-wild benchmark for AI agents in the production harness.
  - 推荐理由：当前 GitHub stars 约 536，说明已经形成一定关注度；近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度；属于近 24 小时内的新鲜动态
  - 关键信号：开源类型：面向 AI agent 或编码助手的开源项目；GitHub stars：536；信号来源：GitHub 发现流。
  - 原文摘要：An in-the-wild benchmark for AI agents in the production harness.

- [InternLM/Intern-Decision is trending](https://github.com/InternLM/Intern-Decision)
  - 中文说明：主体：InternLM；事件类型：开源项目发布；来源：GitHub 发现流；评分：70.26；标签：未打标签。
  - 摘要：`InternLM/Intern-Decision` 最近进入 GitHub 高活跃区间，属于围绕模型权重、模型推理或模型家族的开源项目。Fast multi-modal decision model
  - 推荐理由：当前 GitHub stars 约 822，说明已经形成一定关注度；近期在 GitHub 发现流里活跃，适合判断开源生态的真实热度
  - 关键信号：开源类型：围绕模型权重、模型推理或模型家族的开源项目；GitHub stars：822；信号来源：GitHub 发现流。
  - 原文摘要：Fast multi-modal decision model

## 其他观察（15）

### OpenAI（3 条重点）

- [How iFood scales coding agents across 15,000 repositories](https://openai.com/business/customer-stories/ifood)
  - 中文说明：主体：OpenAI；事件类型：观察事项；来源：官方资讯源；评分：54.12；标签：Agent、编程。
  - 摘要：这是官方发布源中的一条更新，核心内容是：How iFood scales coding agents across 15,000 repositories
  - 推荐理由：来自官方发布面，可信度比二手转述更高
  - 关键信号：信号来源：官方 RSS。

- [Searching for distant planets with Astra](https://openai.com/index/searching-for-distant-planets-with-astra)
  - 中文说明：主体：OpenAI；事件类型：观察事项；来源：官方资讯源；评分：27.95；标签：编程。
  - 摘要：这是官方发布源中的一条更新，核心内容是：See how two amateur astronomers used Codex and Astra to find potential exoplanets in public data from NASA’s Kepler and…
  - 推荐理由：来自官方发布面，可信度比二手转述更高
  - 关键信号：信号来源：官方 RSS。
  - 原文摘要：See how two amateur astronomers used Codex and Astra to find potential exoplanets in public data from NASA’s Kepler and TESS space telescopes.

- [How Intentful uses dots to make more time for growth](https://openai.com/business/customer-stories/intentful-dots)
  - 中文说明：主体：OpenAI；事件类型：观察事项；来源：官方资讯源；评分：26.12；标签：未打标签。
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

- [Taking Trainium3 to the Track: Generating Videos with LTX-2.5](https://huggingface.co/blog/video-trainium3)
  - 中文说明：主体：Hugging Face；事件类型：观察事项；来源：官方资讯源；评分：38.12；标签：视频。
  - 摘要：这是官方发布源中的一条更新，核心内容是：Taking Trainium3 to the Track: Generating Videos with LTX-2.5
  - 推荐理由：来自官方发布面，可信度比二手转述更高
  - 关键信号：信号来源：官方 RSS。

- [Building on Nemotron 3.5 Parse: Open Data, Fine-Tuning, and Faster Inference](https://huggingface.co/blog/nvidia/building-on-nemotron-35-parse-open-data-fine-tunin)
  - 中文说明：主体：Hugging Face；事件类型：观察事项；来源：官方资讯源；评分：34.97；标签：基础设施。
  - 摘要：这是官方发布源中的一条更新，核心内容是：Building on Nemotron 3.5 Parse: Open Data, Fine-Tuning, and Faster Inference
  - 推荐理由：来自官方发布面，可信度比二手转述更高
  - 关键信号：信号来源：官方 RSS。

- [Hill-climbing Inkling 2 Mini inference on one RTX PRO 6000](https://huggingface.co/blog/inkling-2-mini-inference-hillclimb)
  - 中文说明：主体：Hugging Face；事件类型：观察事项；来源：官方资讯源；评分：30.12；标签：基础设施。
  - 摘要：这是官方发布源中的一条更新，核心内容是：Hill-climbing Inkling 2 Mini inference on one RTX PRO 6000
  - 推荐理由：来自官方发布面，可信度比二手转述更高
  - 关键信号：信号来源：官方 RSS。

### NVIDIA AI（3 条重点）

- [Come for the Games, Stay for the Community With GeForce NOW](https://blogs.nvidia.com/blog/geforce-now-thursday-community-war-thunder-reward/)
  - 中文说明：主体：NVIDIA AI；事件类型：观察事项；来源：官方资讯源；评分：36.46；标签：未打标签。
  - 摘要：这是官方发布源中的一条更新，核心内容是：Good games bring people together. This GFN Thursday, GeForce NOW is celebrating the members, creators and community mod…
  - 推荐理由：来自官方发布面，可信度比二手转述更高
  - 关键信号：信号来源：官方 RSS。
  - 原文摘要：Good games bring people together. This GFN Thursday, GeForce NOW is celebrating the members, creators and community moderators who turn every session into something worth sharing.…

- [Merry Making: Play, Build and Create With NVIDIA Technologies This Holiday Season](https://blogs.nvidia.com/blog/nvidia-technologies-holidays-2026/)
  - 中文说明：主体：NVIDIA AI；事件类型：观察事项；来源：官方资讯源；评分：24.95；标签：未打标签。
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
