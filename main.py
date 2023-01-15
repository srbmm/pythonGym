from classes.Menu import Menu
from classes.Gym import Gym

my_gym = Gym()
my_app = Menu({
    "add athlete to gym: ": my_gym.add,
    "show all athlete: ": my_gym.print_all,
    "find athlete: ": my_gym.find_and_print
})
my_app.run()
