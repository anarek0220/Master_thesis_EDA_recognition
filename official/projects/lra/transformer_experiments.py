# Copyright 2022 The TensorFlow Authors. All Rights Reserved.
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
"""Transformer experiments."""
# pylint: disable=g-doc-return-or-yield,line-too-long
import dataclasses

from official.core import config_definitions as cfg
from official.core import exp_factory
from official.modeling import optimization
from official.nlp.configs import encoders
from official.nlp.data import sentence_prediction_dataloader
from official.nlp.tasks import sentence_prediction

from official.projects.lra import lra_dual_encoder_dataloader
from official.projects.lra import lra_dual_encoder_task
from official.projects.lra.transformer import TransformerEncoderConfig

AdamWeightDecay = optimization.AdamWeightDecayConfig
PolynomialLr = optimization.PolynomialLrConfig
PolynomialWarmupConfig = optimization.PolynomialWarmupConfig


@dataclasses.dataclass
class TransformerOptimizationConfig(optimization.OptimizationConfig):
  """Transformer optimization configuration."""
  optimizer: optimization.OptimizerConfig = optimization.OptimizerConfig(
      type='adamw',
      adamw=AdamWeightDecay(
          weight_decay_rate=0.01,
          exclude_from_weight_decay=['LayerNorm', 'layer_norm', 'bias'],
          epsilon=1e-6))
  learning_rate: optimization.LrConfig = optimization.LrConfig(
      type='polynomial',
      polynomial=PolynomialLr(initial_learning_rate=1e-4,
                              decay_steps=1000000,
                              end_learning_rate=0.0))
  warmup: optimization.WarmupConfig = optimization.WarmupConfig(
      type='polynomial', polynomial=PolynomialWarmupConfig(warmup_steps=10000))


@exp_factory.register_config_factory('transformer/lra_listops')
def transformer_listops() -> cfg.ExperimentConfig:
  """Transformer lra fine-tuning."""
  config = cfg.ExperimentConfig(
      task=sentence_prediction.SentencePredictionConfig(
          model=sentence_prediction.ModelConfig(encoder=encoders.EncoderConfig(
              type='any', any=TransformerEncoderConfig())),
          train_data=sentence_prediction_dataloader.
          SentencePredictionDataConfig(),
          validation_data=sentence_prediction_dataloader.
          SentencePredictionDataConfig(is_training=False,
                                       drop_remainder=False)),
      trainer=cfg.TrainerConfig(
          optimizer_config=optimization.OptimizationConfig({
              'optimizer': {
                  'type': 'adamw',
                  'adamw': {
                      'weight_decay_rate':
                          0.01,
                      'exclude_from_weight_decay':
                          ['LayerNorm', 'layer_norm', 'bias'],
                  }
              },
              'learning_rate': {
                  'type': 'polynomial',
                  'polynomial': {
                      'initial_learning_rate': 3e-5,
                      'end_learning_rate': 0.0,
                  }
              },
              'warmup': {
                  'type': 'polynomial'
              }
          })))
  return config


@exp_factory.register_config_factory('transformer/lra_imdb')
def transformer_imdb() -> cfg.ExperimentConfig:
  """Transformer lra fine-tuning."""
  config = cfg.ExperimentConfig(
      task=sentence_prediction.SentencePredictionConfig(
          model=sentence_prediction.ModelConfig(encoder=encoders.EncoderConfig(
              type='any', any=TransformerEncoderConfig())),
          train_data=sentence_prediction_dataloader.
          SentencePredictionDataConfig(),
          validation_data=sentence_prediction_dataloader.
          SentencePredictionDataConfig(is_training=False,
                                       drop_remainder=False)),
      trainer=cfg.TrainerConfig(
          optimizer_config=optimization.OptimizationConfig({
              'optimizer': {
                  'type': 'adamw',
                  'adamw': {
                      'weight_decay_rate':
                          0.01,
                      'exclude_from_weight_decay':
                          ['LayerNorm', 'layer_norm', 'bias'],
                  }
              },
              'learning_rate': {
                  'type': 'polynomial',
                  'polynomial': {
                      'initial_learning_rate': 3e-5,
                      'end_learning_rate': 0.0,
                  }
              },
              'warmup': {
                  'type': 'polynomial'
              }
          })))
  return config


@exp_factory.register_config_factory('transformer/lra_cifar')
def transformer_cifar() -> cfg.ExperimentConfig:
  """Transformer lra fine-tuning."""
  config = cfg.ExperimentConfig(
      task=sentence_prediction.SentencePredictionConfig(
          model=sentence_prediction.ModelConfig(encoder=encoders.EncoderConfig(
              type='any', any=TransformerEncoderConfig())),
          train_data=sentence_prediction_dataloader.
          SentencePredictionDataConfig(),
          validation_data=sentence_prediction_dataloader.
          SentencePredictionDataConfig(is_training=False,
                                       drop_remainder=False)),
      trainer=cfg.TrainerConfig(
          optimizer_config=optimization.OptimizationConfig({
              'optimizer': {
                  'type': 'adamw',
                  'adamw': {
                      'weight_decay_rate':
                          0.0,
                      'exclude_from_weight_decay':
                          ['LayerNorm', 'layer_norm', 'bias'],
                  }
              },
              'learning_rate': {
                  'type': 'polynomial',
                  'polynomial': {
                      'initial_learning_rate': 3e-5,
                      'end_learning_rate': 0.0,
                  }
              },
              'warmup': {
                  'type': 'polynomial'
              }
          })))
  return config


@exp_factory.register_config_factory('transformer/lra_pathfinder')
def transformer_pathfinder() -> cfg.ExperimentConfig:
  """Transformer lra fine-tuning."""
  config = cfg.ExperimentConfig(
      task=sentence_prediction.SentencePredictionConfig(
          model=sentence_prediction.ModelConfig(encoder=encoders.EncoderConfig(
              type='any', any=TransformerEncoderConfig())),
          train_data=sentence_prediction_dataloader.
          SentencePredictionDataConfig(),
          validation_data=sentence_prediction_dataloader.
          SentencePredictionDataConfig(is_training=False,
                                       drop_remainder=False)),
      trainer=cfg.TrainerConfig(
          optimizer_config=optimization.OptimizationConfig({
              'optimizer': {
                  'type': 'adamw',
                  'adamw': {
                      'weight_decay_rate':
                          0.0,
                      'exclude_from_weight_decay':
                          ['LayerNorm', 'layer_norm', 'bias'],
                  }
              },
              'learning_rate': {
                  'type': 'polynomial',
                  'polynomial': {
                      'initial_learning_rate': 3e-5,
                      'end_learning_rate': 0.0,
                  }
              },
              'warmup': {
                  'type': 'polynomial'
              }
          })))
  return config


@exp_factory.register_config_factory('transformer/lra_aan')
def transformer_aan() -> cfg.ExperimentConfig:
  """Transformer lra fine-tuning."""
  config = cfg.ExperimentConfig(
      task=lra_dual_encoder_task.DualEncoderConfig(
          model=lra_dual_encoder_task.ModelConfig(
              encoder=encoders.EncoderConfig(type='any',
                                             any=TransformerEncoderConfig())),
          train_data=lra_dual_encoder_dataloader.DualEncoderDataConfig(),
          validation_data=lra_dual_encoder_dataloader.DualEncoderDataConfig(
              is_training=False, drop_remainder=False)),
      trainer=cfg.TrainerConfig(
          optimizer_config=optimization.OptimizationConfig({
              'optimizer': {
                  'type': 'adamw',
                  'adamw': {
                      'weight_decay_rate':
                          0.1,
                      'exclude_from_weight_decay':
                          ['LayerNorm', 'layer_norm', 'bias'],
                  }
              },
              'learning_rate': {
                  'type': 'polynomial',
                  'polynomial': {
                      'initial_learning_rate': 3e-5,
                      'end_learning_rate': 0.0,
                  }
              },
              'warmup': {
                  'type': 'polynomial'
              }
          })))
  return config
