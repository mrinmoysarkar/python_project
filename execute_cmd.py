def execute_cmd(cmd):
    import json
    import difflib
    from speak import speak
    import os
    from play_audio import play_song
    
    threshold = 0.8 # matching probability cutoff
    json_file = open("Minion_Q.json")
    data = json.load(json_file)
    json_file.close()
    
    questions = data.keys()
    qstn = difflib.get_close_matches(cmd, questions, cutoff=threshold )
    if qstn:
        ans = data[qstn[0]]
        if ans == "play":
            play_song(qstn[0])
        elif qstn[0] == "stop song":
            os.system('pkill mpg321')
        elif ans:
            speak(ans)
    else:
        print "command is not found in database."
