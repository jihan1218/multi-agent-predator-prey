import tensorflow as tf
import gym
import time

from ppo_pkg.ppo import ppo
from mae_envs.envs import hide_and_seek
from ma_policy.ma_policy import MAPolicy
from testing.test_policy import test_ppo

env_fn = lambda: hide_and_seek.make_env()  # choose desired environment

dir_str = '../Testing/exp/'  # set output directory

now_str = time.asctime(time.localtime())  # get current time stamp and set logger dict
logger_kwargs = dict(output_dir=dir_str + now_str, exp_name='hide_and_seek')  # for saving information during training

ppo(env_fn=env_fn,  # run ppo training loop (check ppo.py for documentation)
    pi_lr=3e-4,
    vf_lr=3e-4,
    steps_per_epoch=10000,
    epochs=1000,
    train_pi_iters=50,
    train_v_iters=50,
    logger_kwargs=logger_kwargs)

test_ppo(dir_str + now_str)  # test learned policy
