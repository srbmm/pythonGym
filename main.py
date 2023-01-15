from classes.Menu import Menu

test = Menu({
    "gozie yek": lambda : print("yek"),
    "gozine do": lambda : print("do"),
    "gozine se": lambda :print("se")
})
test.run()
