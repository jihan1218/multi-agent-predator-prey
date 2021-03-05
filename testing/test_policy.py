from spinup.utils.test_policy import load_policy_and_env, run_policy
from mae_envs.envs import hide_and_seek


def test_ppo(exp_dir, itr='last'):
    _, get_action, lstm = load_policy_and_env(exp_dir, itr=itr)
    env = hide_and_seek.make_env()
    run_policy(env, get_action, lstm=lstm)
