# Game Direction
A rummy-inspired card game about debt, consequences, and information.

# Dev Environment Setup

~~Run `setup_dev_environment.sh`.~~

If in a Codespace: 
1. Start an x server by running `start-gui.sh`. 
2. Navigate over to the "Ports" tab in the bottom menu and find port "6080"
3. Set port 6080 to public
4. Open that link in the browser!
5. Click on `vnc_auto.html@` from the list of files to open the noVNC server

# Dev Diary

## 2025-12-19

This has been an uphill battle the whole way. Now, `start_gui.sh` no longer starts a functional noVNC server. Sometimes, manually running `x11vnc -display :1 -nopw -forever -shared -rfbport 5900` does the trick.


## 2025-12-18

Okay, solution: I just won't test pygame visuals until I'm at a workstation that I can cross-compile code on (or just not bother at all). It's definitely got the vibes of giving up, but I've had it I tell you!

~~Here's a thought: What if I just *don't* build it around Pygame? Just make an ASCII game instead!~~

**GOOD NEWS EVERYONE!!** Who needs ASCII when you can just launch a noVNC server? Now we're cooking with grease!

**BAD NEWS EVERYONE!!** Straights aren't calculating properly. Must do unit testing!!

**GOOD NEWS EVERYONE!!** There's no more bold-text bearing news. 

## 2025-12-17

Progress has been made, we have sucessfully built the code and had it run without exploding. Hooray!

Huge, *glaring* problem: in order to test on Windows I currently have to use a Github action. That's stupid and leads to very annoyed git commit messages. 

How do I fix this? No clue!


## 2025-12-16

That's it, I've had it! I try to learn PyGame, and I'm defeated by my own incompetence.

I try to learn unit testing to help validate my work in an environment that lacks an X server, and I'm defeated there!

I quit, I'm putting this down for today. 

## 2025-12-12

To do: 

- Learn workflows to compile to different platforms 
- Make my workflow names more obvious
- Start PyGaming?