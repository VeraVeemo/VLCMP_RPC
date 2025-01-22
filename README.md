

# **IMPORTANT NOTICE!**

If you need help, contact me on discord! (Profile link is the first link on my profile)

## First Step: The Discord Application setup

You're going to need a Discord Application!
 You can create one here: https://discord.com/developers/applications.

Once you're on the page, press the "New Application" button.

![image_2025-01-22_205531361](https://github.com/user-attachments/assets/d5f654db-0ac0-4e9d-810a-47c5f886b755)

Once you press it, you should see a pop up like this:

![image_2025-01-22_205628120](https://github.com/user-attachments/assets/5cc19208-5e76-45f9-a909-8c944a4eea9d)

If you do, give it a name, tick the checkbox, and press "Create".

( For the name I'd recommend VLC Media Player as it'll show up as "Playing __" whatever you put instead. )

Now, if you managed to do all of that then you should end up on a page with the link "https://discord.com/developers/applications/{APPLICATION_ID}/information", and if you did; well done! You did the job most people cant!

Next, you're going to want to copy the Application ID. You can do this by either copying it from the link or pressing the "Copy ID" button under the Application ID itself on the page, and then save it for later.

![image](https://github.com/user-attachments/assets/b0007874-5e42-44d9-ac17-72ed78995916)

Now for the least fun part, waiting!
 On the left bar, there should be a bunch of buttons. Now leave your pea brain alone for a second and focus on the "Rich Presence" button.

![image](https://github.com/user-attachments/assets/c71d690a-6966-415f-b804-e27424bd75a5)

You're going to want to click it, it should bring up a new page with a bunch of crap on it. You're going to ignore all of that and focus on the bottom of the page, the Assets!

 Click the button "Add Image" and it should bring a popup on uploading an image.

![image](https://github.com/user-attachments/assets/092b581c-546e-489b-ad51-6996bd46f90e)

Now I have a premade image for you here since I'm so kind, it's a png so don't worry (It's also the minimum size)

![image_2025-01-22_210702376](https://github.com/user-attachments/assets/34875929-ed47-45a4-96bb-5adec60b0716)

Now once you have the image downloaded and uploaded to the Discord Application, you're going to have name it "vlc_logo" otherwise your RPC will have a blank image, unless you want that.

(Should look like this)

![image](https://github.com/user-attachments/assets/7dc887e3-c167-4fce-86c6-be3458bb2565)

Press "Save Changes" and wait about 5-15 minutes since Discord is verifying your image is safe and abides their Guidelines.

In the meantime, let's get on to the second part.

## Second Step: VLC Media Player HTTP Request setup

This is the most boring and annoying part of this entire thing since it's literally just clicking random stuff, but anywho let's get on with this I'm tired of typing.

Now you're going want to open VLC Media Player (Download it if you haven't already; https://www.videolan.org)

Once you're in VLC, press Ctrl + P to open preferences, or press Tools, and scroll down to Preferences and click it.

After you've opened preferences, go to the bottom left of the window and press "All" option on the "View Settings" section.

![image](https://github.com/user-attachments/assets/7d3de452-e1bc-4e07-becd-7548c216ede0)

You're going to want to scroll down on the left section until you reach "Interface" then you're going to want to open the dropdown (If it already isn't open) and it should come up with something like this:

![image](https://github.com/user-attachments/assets/70a96ecd-6f6e-4608-a2f7-3327563f5ea4)

Then you're going to want to click "Main Interfaces", on the section on the right, enable "Web" and the box below should have "http" in it.

![image](https://github.com/user-attachments/assets/0f78e465-7240-44fe-8edc-cd0232ab8d11)

Once you've done that, go back to the left section and open the dropdown for "Main Interfaces". You're going to want to click Lua.
 After you've clicked Lua, the right section should have "Lua interpreter". Go down to "Lua HTTP" and set your password.

 ![image](https://github.com/user-attachments/assets/427b2f42-9bc4-4c35-9668-3d30eb319662)

After you set your password, press save, exit preferences, and **restart VLC**.
 If you've done it head to this link = http://localhost:8080/requests/status.json and it should pop up with a user and password login, leave user empty and enter the password you just typed into VLC.
  If it shows any JSON data it means you've done it all correctly, you can safely close this tab since we won't need it (only the code does).

And that's second step done!

## Third Step: scary variable setup 😱😱
For running the code, I don't reccomend using Python itself since infinite while loops (which is what the code uses to update your RPC constantly) doesn't work well.

I'd recommend download PyCharm since it's user friendly (link here: https://www.jetbrains.com/pycharm/download)

Once you've downloaded PyCharm, don't open it just yet we'll need it in like 5 minutes. For now we need to make the Python file.

If you have python installed, (download link here: https://www.python.org/downloads) you should have an app called "IDLE" open this app up.
 Once you have it should come up with this:

![image](https://github.com/user-attachments/assets/8410048d-ae1d-458b-a512-de5bb6ea288d)

Press CTRL + S immediately and save it to a location where you'll remember.

Now open up PyCharm and press "New Project"

![image](https://github.com/user-attachments/assets/974059a9-bb67-4a13-8407-51c70a0cef2a)

Press "Create" and then once it's done doing its business (progress bar on bottom bar), drag and drop the .py file you made from IDLE onto the right section.

Once it's done loading the file, press CTRL + A to quickly select all text and press BACKSPACE to delete it all. (We don't need the copyright crap).

Now since PyCharm luckily automatically makes an enviornment, you're going to want to click the 3 Layer thing (Image stolen from the friend I helped on discord)

![image](https://github.com/user-attachments/assets/613eca95-ce1d-450f-a793-0260fac5be9d)

Once you have, type in "pypresence" and install the top result, after you've done that type in "requests" and install the top result.

After it's done downloading all the files, copy and paste the code from this Respoitory.

Now, you will only need 2 things to fill out;

The "client_id" which is your Discord Application ID from first step.

And your "vlc_pass" which is the password you set for VLC from second step.

![image](https://github.com/user-attachments/assets/9fc06784-5872-4a0f-8ba7-8d78bd6603e4)

Now all you have to do is hit "Run" (the button that looks like play)

![image](https://github.com/user-attachments/assets/a02e5551-8ff7-4c5c-9761-0edffa996d6c)

Aaand you're done! Check Discord and your RPC should be set.
