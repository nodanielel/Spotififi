import flet as ft
import flet_audio as fta

def main(page: ft.Page):

    songs = [{"src": "sound/song1.mp3", "title": "Who Knows", "artist": "Daniel Caesar", "album": "Case Study 01"}, {"src": "sound/song2.mp3", "title": "The Ghost of You", "artist": "My Chemical Romance", "album": "Three Cheers for Sweet Revenge"},
        {"src": "sound/song3.mp3", "title": "Crying Lightning", "artist": "Arctic Monkeys", "album": "Humbug"},
        {"src": "sound/song4.mp3", "title": "Do I Wanna Know?", "artist": "Arctic Monkeys", "album": "AM"},
        {"src": "sound/song5.mp3", "title": "Breathe", "artist": "Malcolm Todd", "album": "Unknown"},]

    current_index = 0

    async def playAudio(e):
        await audio1.play()
    
    async def pauseAudio(e):
        await audio1.pause()
    
    async def resumeAudio(e):
        await audio1.resume()

    async def getAudioDuration():
        duration = await audio1.get_duration()
       

    async def getSongPosition():
        position = await audio1.get_current_position()
        positionText.value = f"Minutos: {position.minutes:02}:{position.seconds:02}"

    async def nextSong(e):
        nonlocal current_index
        await audio1.pause() 

        current_index += 1
        if current_index >= len(songs):
            current_index = 0

        loadSong()
        await audio1.resume() 
    async def prevSong(e):
        nonlocal current_index
        await audio1.pause()  

        current_index -= 1
        if current_index < 0:
            current_index = len(songs) - 1

        loadSong()
        await audio1.resume()  
    def changeVolume(e):
        audio1.volume = volumeSlider.value/100

    def loadSong():
        audio1.src = songs[current_index]["src"]
        titleText.value = f"Title: {songs[current_index]['title']}"
        artistText.value = f"Artist: {songs[current_index]['artist']}"
        albumText.value = f"Album: {songs[current_index]['album']}"
        page.update()

    audio1 = fta.Audio(src="sound/song1.mp3", on_position_change=getSongPosition)

    playButton = ft.Button(content="Play", on_click=playAudio)
    pauseButton = ft.Button(content="Pause", on_click=pauseAudio)
    resumeButton = ft.Button(content="Resume", on_click=resumeAudio)

    nextButton = ft.Button(content="Next", on_click=nextSong)
    prevButton = ft.Button(content="Previous", on_click=prevSong)

    volumeSlider = ft.Slider(value=100, divisions=100, max=100, min=0, on_change=changeVolume)

   
    positionText = ft.Text(value="Minutos: ")

    titleText = ft.Text(value=f"Title: {songs[current_index]['title']}")
    artistText = ft.Text(value=f"Artist: {songs[current_index]['artist']}")
    albumText = ft.Text(value=f"Album: {songs[current_index]['album']}")

    page.add(titleText,artistText,albumText,playButton,pauseButton,resumeButton,prevButton,nextButton,volumeSlider,positionText)

ft.run(main=main, assets_dir="assets")