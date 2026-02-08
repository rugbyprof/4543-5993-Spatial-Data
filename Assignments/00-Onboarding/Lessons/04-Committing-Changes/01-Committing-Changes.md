## Making and Committing Changes

One thing about working in CodeSpaces is that we need to ensure that any changes or additions you make to your code need to find themselves back to your original repository. This may sound a little weird, because it simply looks like you are already editing your repository, and you are! However, the point behind version control is that any changes you make haven't really happened until you "commit" them to a branch ("main" in our case). So let me walk your through it.

### 1️⃣ Create a file

- In your file explorer, right click and choose "new file".
- It will give you a box to type the name in. Call your new file "hello.py".

### 2️⃣ Edit File

- Click on your new file `hello.py` in the file explorer and the editor portion of your environment will show you the contents of that file. It's empty, obviously.
- Add one line of code: `print("hello world")`. Seems cheesy, but we only need to understand how to commit changes and make them permanent.

### 3️⃣ Run the File

- Before we commit our changes, lets run the file.
- Go to the terminal and type `ll` (double L) and hit enter.
- You should see the same thing that is in the file explorer to the left.
- Do you see your `hello.py` file?
- If so, type this command: `python hello.py` and hit enter.
- You should see "hello world" printed out.

### 4️⃣ Committing Changes

- After you added the `hello.py` file. You should see a blue 1 over the source control icon (looks like a 3 node graph).
- Click on that icon and it will give you a different view that has a button that say's commit, and a txt box to comment on what your committing.
- In the txt box type "Added hello.py"
- Then click commit.
- Click "Always" on the box that pops up.
- Then click "Sync Changes"
- Then click "Ok, and don't show again"
- Finally go back to your repo on github and refresh the page.
