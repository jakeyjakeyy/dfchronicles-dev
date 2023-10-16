def SaveWorld(root, owner):
    from chronicle_compiler import models

    # testing
    # return models.World.objects.get(id=271)

    owner = models.User.objects.get(id=1)
    if root[1].tag == 'altname':
        world = models.World.objects.create(name=root[1].text, name2=root[0].text, owner=owner)
        world.save()
    return world
