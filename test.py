import easyttuimenus as ttui # pyright: ignore[reportMissingTypeStubs]
options = ["cherry", "apple", "banana"]
picked = ttui.multiple_choice_menu("Here's some fruit", options)
print(picked)