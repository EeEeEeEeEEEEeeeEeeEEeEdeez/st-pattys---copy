sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite, otherSprite) {
    game.gameOver(true)
})
music.play(music.createSong(assets.song`the next episode`), music.PlaybackMode.LoopingInBackground)
