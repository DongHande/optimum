# coding=utf-8
# Copyright 2022 The HuggingFace Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

VALIDATE_EXPORT_ON_SHAPES_SLOW = {
    "batch_size": [2, 4, 6],
    "sequence_length": [8, 17, 33, 64, 96, 154],
    "num_choices": [2, 4],
}

VALIDATE_EXPORT_ON_SHAPES_FAST = {
    "batch_size": [4],
    "sequence_length": [19],
    "num_choices": [4],
}


PYTORCH_EXPORT_MODELS_TINY = {
    "albert": "hf-internal-testing/tiny-random-AlbertModel",
    "beit": "hf-internal-testing/tiny-random-BeitForImageClassification",
    "bert": "hf-internal-testing/tiny-random-BertModel",
    "bart": "hf-internal-testing/tiny-random-bart",
    "big-bird": "hf-internal-testing/tiny-random-BigBirdModel",
    "bigbird-pegasus": "hf-internal-testing/tiny-random-bigbird_pegasus",
    "blenderbot-small": "hf-internal-testing/tiny-random-BlenderbotModel",
    "blenderbot": "hf-internal-testing/tiny-random-BlenderbotModel",
    "bloom": "hf-internal-testing/tiny-random-BloomModel",
    "camembert": "hf-internal-testing/tiny-random-camembert",
    "clip": "hf-internal-testing/tiny-random-CLIPModel",
    "convbert": "hf-internal-testing/tiny-random-ConvBertModel",
    "codegen": "hf-internal-testing/tiny-random-CodeGenModel",
    "data2vec-text": "hf-internal-testing/tiny-random-Data2VecTextModel",
    "data2vec-vision": "hf-internal-testing/tiny-random-Data2VecVisionModel",
    "deberta": "hf-internal-testing/tiny-random-DebertaModel",
    "deberta-v2": "hf-internal-testing/tiny-random-DebertaV2Model",
    "deit": "hf-internal-testing/tiny-random-DeiTModel",
    "convnext": "hf-internal-testing/tiny-random-convnext",
    "detr": "hf-internal-testing/tiny-random-detr",
    "distilbert": "hf-internal-testing/tiny-random-DistilBertModel",
    "electra": "hf-internal-testing/tiny-random-ElectraModel",
    "flaubert": "hf-internal-testing/tiny-random-flaubert",
    "gpt2": "hf-internal-testing/tiny-random-gpt2",
    "gpt-neo": "hf-internal-testing/tiny-random-GPTNeoModel",
    "gptj": "hf-internal-testing/tiny-random-GPTJModel",
    "groupvit": "hf-internal-testing/tiny-random-groupvit",
    "ibert": "hf-internal-testing/tiny-random-IBertModel",
    "levit": "hf-internal-testing/tiny-random-LevitModel",
    "layoutlm": "hf-internal-testing/tiny-random-LayoutLMModel",
    "layoutlmv3": "hf-internal-testing/tiny-random-LayoutLMv3Model",
    "longt5": "hf-internal-testing/tiny-random-LongT5Model",
    # "longformer": "allenai/longformer-base-4096",
    "m2m-100": "hf-internal-testing/tiny-random-m2m_100",
    "marian": "sshleifer/tiny-marian-en-de",  # hf-internal-testing ones are broken
    "mbart": "hf-internal-testing/tiny-random-mbart",
    "mobilebert": "hf-internal-testing/tiny-random-MobileBertModel",
    # "mobilenet_v1": "google/mobilenet_v1_0.75_192",
    # "mobilenet_v2": "google/mobilenet_v2_0.35_96",
    "mobilevit": "hf-internal-testing/tiny-random-mobilevit",
    "mt5": "lewtun/tiny-random-mt5",
    # "owlvit": "google/owlvit-base-patch32",
    "perceiver": {
        "hf-internal-testing/tiny-random-language_perceiver": ["masked-lm", "sequence-classification"],
        "hf-internal-testing/tiny-random-vision_perceiver_conv": ["image-classification"],
    },
    # "rembert": "google/rembert",
    "resnet": "hf-internal-testing/tiny-random-resnet",
    "roberta": "hf-internal-testing/tiny-random-RobertaModel",
    "roformer": "hf-internal-testing/tiny-random-RoFormerModel",
    "segformer": "hf-internal-testing/tiny-random-SegformerModel",
    "squeezebert": "hf-internal-testing/tiny-random-SqueezeBertModel",
    "swin": "hf-internal-testing/tiny-random-SwinModel",
    "t5": "hf-internal-testing/tiny-random-t5",
    "vit": "hf-internal-testing/tiny-random-vit",
    "yolos": "hf-internal-testing/tiny-random-YolosModel",
    "whisper": "openai/whisper-tiny.en",  # hf-internal-testing ones are broken
    "xlm": "hf-internal-testing/tiny-random-XLMModel",
    "xlm-roberta": "hf-internal-testing/tiny-xlm-roberta",
}


PYTORCH_EXPORT_MODELS_LARGE = {
    "albert": "albert-base-v2",
    "beit": "microsoft/beit-base-patch16-224",
    "bert": "bert-base-cased",
    "bart": "facebook/bart-base",
    "big-bird": "google/bigbird-roberta-base",
    "bigbird-pegasus": "hf-internal-testing/tiny-random-bigbird_pegasus",  # Not using google/bigbird-pegasus-large-arxiv because it takes too much time for testing.
    "blenderbot-small": "facebook/blenderbot_small-90M",
    "blenderbot": "facebook/blenderbot-90M",
    "bloom": "hf-internal-testing/tiny-random-BloomModel",  # Not using bigscience/bloom-560m because it goes OOM.
    "camembert": "camembert-base",
    "clip": "openai/clip-vit-base-patch32",
    "convbert": "YituTech/conv-bert-base",
    "codegen": "hf-internal-testing/tiny-random-CodeGenModel",  # Not using Salesforce/codegen-350M-multi because it takes too much time for testing.
    "data2vec-text": "facebook/data2vec-text-base",
    "data2vec-vision": "facebook/data2vec-vision-base",
    "deberta": "hf-internal-testing/tiny-random-DebertaModel",  # Not using microsoft/deberta-base because it takes too much time for testing.
    "deberta-v2": "hf-internal-testing/tiny-random-DebertaV2Model",  # Not using microsoft/deberta-v2-xlarge because it takes too much time for testing.
    "deit": "facebook/deit-small-patch16-224",
    "convnext": "facebook/convnext-tiny-224",
    "detr": "hf-internal-testing/tiny-random-detr",  # Not using facebook/detr-resnet-50 because it takes too much time for testing.
    "distilbert": "distilbert-base-cased",
    "electra": "google/electra-base-generator",
    "flaubert": "hf-internal-testing/tiny-random-flaubert",  # TODO
    "gpt2": "gpt2",
    "gpt-neo": "EleutherAI/gpt-neo-125M",
    "gptj": "anton-l/gpt-j-tiny-random",  # TODO
    "groupvit": "nvidia/groupvit-gcc-yfcc",
    "ibert": "kssteven/ibert-roberta-base",
    "levit": "facebook/levit-128S",
    "layoutlm": "microsoft/layoutlm-base-uncased",
    "layoutlmv3": "microsoft/layoutlmv3-base",
    "longt5": "hf-internal-testing/tiny-random-longt5",  # Not using google/long-t5-local-base because it takes too much time for testing.
    # "longformer": "allenai/longformer-base-4096",
    "m2m-100": "hf-internal-testing/tiny-random-m2m_100",  # Not using facebook/m2m100_418M because it takes too much time for testing.
    "marian": "Helsinki-NLP/opus-mt-en-de",
    "mbart": "sshleifer/tiny-mbart",
    "mobilebert": "google/mobilebert-uncased",
    # "mobilenet_v1": "google/mobilenet_v1_0.75_192",
    # "mobilenet_v2": "google/mobilenet_v2_0.35_96",
    "mobilevit": "apple/mobilevit-small",
    "mt5": "lewtun/tiny-random-mt5",  # Not using google/mt5-small because it takes too much time for testing.
    "owlvit": "google/owlvit-base-patch32",
    "perceiver": "hf-internal-testing/tiny-random-PerceiverModel",  # Not using deepmind/language-perceiver because it takes too much time for testing.
    # "rembert": "google/rembert",
    "resnet": "microsoft/resnet-50",
    "roberta": "roberta-base",
    "roformer": "junnyu/roformer_chinese_base",
    "segformer": "nvidia/segformer-b0-finetuned-ade-512-512",
    "squeezebert": "squeezebert/squeezebert-uncased",
    "swin": "microsoft/swin-tiny-patch4-window7-224",
    "t5": "t5-small",
    "vit": "google/vit-base-patch16-224",
    "yolos": "hustvl/yolos-tiny",
    "whisper": "openai/whisper-tiny.en",
    "xlm": "xlm-clm-ende-1024",
    "xlm-roberta": "Unbabel/xlm-roberta-comet-small",
}

TENSORFLOW_EXPORT_MODELS = {
    "albert": "hf-internal-testing/tiny-albert",
    "bert": "bert-base-cased",
    "camembert": "camembert-base",
    "distilbert": "distilbert-base-cased",
    "roberta": "roberta-base",
}

PYTORCH_STABLE_DIFFUSION_MODEL = {
    ("hf-internal-testing/tiny-stable-diffusion-torch"),
}