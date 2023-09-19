def on_on_overlap(sprite, otherSprite):
    game.game_over(True)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

scene.set_background_color(1)
mySprite = sprites.create(img("""
        ..........................................
            ..........................................
            ..........................................
            ..........................................
            ffffffffffffffffffffffffffffffffffffffffff
            f1111f1ffff1fff1f11111f11ffffff1ff1fffff1f
            f1ff1f1ffff1fff1f1fffff1f1ffff1f1ff1fff1ff
            f1ff1f1ffff1fff1f1fffff1ff1fff1f1fff1f1fff
            f1111f1ffff1fff1f11111f1f1ffff1f1ffff1ffff
            f1ff1f1ffff1fff1f1fffff11ffff11111fff1ffff
            f1ff1f1ffff1fff1f1fffff1f1ff1fffff1ff1ffff
            f1111f1111ff111ff11111f1ff1f1fffff1ff1ffff
            ffffffffffffffffffffffffffffffffffffffffff
            ..........................................
            ..........................................
            ..........................................
    """),
    SpriteKind.player)
controller.move_sprite(mySprite)
mySprite.set_velocity(100, -100)
mySprite.set_bounce_on_wall(True)
corner = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . 1 . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.food)
corner.set_position(-2, -1)
corner_2 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . 1 . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.food)
corner_2.set_position(152, -4)
mySprite.start_effect(effects.trail)
corner_3 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . 1 . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.food)
corner_3.set_position(0, 112)