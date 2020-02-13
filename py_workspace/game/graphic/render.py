#render.py

MODULE_NAME = 'render' 

def render_test():
    print('-render::renter_test invoked.')
    
    # #절대경로 
    from game.sound.echo import echo_test
    echo_test()
    
    ##상대경로 
    # from ..sound.echo import echo_test
    # echo_test()
    pass



