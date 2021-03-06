from gym.envs.registration import register

register(
    id='hide-and-seek',
    entry_point='mae_envs.envs:hide_and_seek',
)
register(
    id='box-locking',
    entry_point='mae_envs.envs:box_locking'
)
