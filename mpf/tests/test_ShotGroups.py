from mock import MagicMock
from mpf.tests.MpfTestCase import MpfTestCase


class TestShotGroups(MpfTestCase):

    def getConfigFile(self):
        return 'test_shot_groups.yaml'

    def getMachinePath(self):
        return 'tests/machine_files/shots/'

    def start_game(self):
        # shots only work in games so we have to do this a lot
        self.machine.events.post('game_start')
        self.advance_time_and_run()
        self.machine.game.balls_in_play = 1

    def test_events_and_complete(self):
        self.start_game()

        self.mock_event("test_group_default_lit_complete")
        self.mock_event("test_group_default_unlit_complete")
        self.mock_event("test_group_default_lit_hit")
        self.mock_event("test_group_default_unlit_hit")
        self.mock_event("test_group_default_hit")
        self.mock_event("test_group_hit")

        self.hit_and_release_switch("switch_1")

        # it should post events. here for the previous(?) profile state
        self.assertEqual(0, self._events['test_group_default_lit_hit'])
        self.assertEqual(1, self._events['test_group_default_unlit_hit'])
        self.assertEqual(1, self._events['test_group_default_hit'])
        self.assertEqual(1, self._events['test_group_hit'])

        self.hit_and_release_switch("switch_1")

        # it posts the oposite state
        self.assertEqual(0, self._events['test_group_default_lit_complete'])
        self.assertEqual(0, self._events['test_group_default_unlit_complete'])
        self.assertEqual(1, self._events['test_group_default_lit_hit'])
        self.assertEqual(1, self._events['test_group_default_unlit_hit'])
        self.assertEqual(2, self._events['test_group_default_hit'])
        self.assertEqual(2, self._events['test_group_hit'])

        self.hit_and_release_switch("switch_2")
        self.hit_and_release_switch("switch_3")
        self.hit_and_release_switch("switch_4")

        self.assertEqual(1, self._events['test_group_default_lit_complete'])
        self.assertEqual(0, self._events['test_group_default_unlit_complete'])
        self.assertEqual(1, self._events['test_group_default_lit_hit'])
        self.assertEqual(4, self._events['test_group_default_unlit_hit'])
        self.assertEqual(5, self._events['test_group_default_hit'])
        self.assertEqual(5, self._events['test_group_hit'])

    def test_rotate(self):
        self.start_game()

        self.mock_event("test_group_default_lit_complete")

        self.assertEqual("unlit", self.machine.shots.shot_1.active_settings['current_state_name'])
        self.assertEqual("unlit", self.machine.shots.shot_2.active_settings['current_state_name'])
        self.assertEqual("unlit", self.machine.shots.shot_3.active_settings['current_state_name'])
        self.assertEqual("unlit", self.machine.shots.shot_4.active_settings['current_state_name'])

        self.hit_and_release_switch("switch_1")

        self.assertEqual("lit", self.machine.shots.shot_1.active_settings['current_state_name'])
        self.assertEqual("unlit", self.machine.shots.shot_2.active_settings['current_state_name'])
        self.assertEqual("unlit", self.machine.shots.shot_3.active_settings['current_state_name'])
        self.assertEqual("unlit", self.machine.shots.shot_4.active_settings['current_state_name'])

        self.hit_and_release_switch("s_rotate_r")

        self.assertEqual("unlit", self.machine.shots.shot_1.active_settings['current_state_name'])
        self.assertEqual("lit", self.machine.shots.shot_2.active_settings['current_state_name'])
        self.assertEqual("unlit", self.machine.shots.shot_3.active_settings['current_state_name'])
        self.assertEqual("unlit", self.machine.shots.shot_4.active_settings['current_state_name'])

        self.hit_and_release_switch("switch_1")

        self.assertEqual("lit", self.machine.shots.shot_1.active_settings['current_state_name'])
        self.assertEqual("lit", self.machine.shots.shot_2.active_settings['current_state_name'])
        self.assertEqual("unlit", self.machine.shots.shot_3.active_settings['current_state_name'])
        self.assertEqual("unlit", self.machine.shots.shot_4.active_settings['current_state_name'])

        self.hit_and_release_switch("s_rotate_r")

        self.assertEqual("unlit", self.machine.shots.shot_1.active_settings['current_state_name'])
        self.assertEqual("lit", self.machine.shots.shot_2.active_settings['current_state_name'])
        self.assertEqual("lit", self.machine.shots.shot_3.active_settings['current_state_name'])
        self.assertEqual("unlit", self.machine.shots.shot_4.active_settings['current_state_name'])

        self.hit_and_release_switch("s_rotate_r")

        self.assertEqual("unlit", self.machine.shots.shot_1.active_settings['current_state_name'])
        self.assertEqual("unlit", self.machine.shots.shot_2.active_settings['current_state_name'])
        self.assertEqual("lit", self.machine.shots.shot_3.active_settings['current_state_name'])
        self.assertEqual("lit", self.machine.shots.shot_4.active_settings['current_state_name'])

        self.hit_and_release_switch("s_rotate_r")

        self.assertEqual("lit", self.machine.shots.shot_1.active_settings['current_state_name'])
        self.assertEqual("unlit", self.machine.shots.shot_2.active_settings['current_state_name'])
        self.assertEqual("unlit", self.machine.shots.shot_3.active_settings['current_state_name'])
        self.assertEqual("lit", self.machine.shots.shot_4.active_settings['current_state_name'])

        self.hit_and_release_switch("s_rotate_l")

        self.assertEqual("unlit", self.machine.shots.shot_1.active_settings['current_state_name'])
        self.assertEqual("unlit", self.machine.shots.shot_2.active_settings['current_state_name'])
        self.assertEqual("lit", self.machine.shots.shot_3.active_settings['current_state_name'])
        self.assertEqual("lit", self.machine.shots.shot_4.active_settings['current_state_name'])