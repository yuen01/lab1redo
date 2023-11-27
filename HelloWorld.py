# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def test_setup_new_user(name):
    print(f'Hi, {name}')
    #git config -- global user.name "name"
    #git config -- global user.email email@ichat.sp.edu.sg

def new_folder(name):
    print(f'Hi, {name}')
    #mkdir name to create a new file
    #mkdir name to create a new file
    #mkdir name to create a new file
    #mkdir name to create a new file
    #mkdir name to create a new file
    #git init to create .git

def new_py_file(name):
    print(f'Hi, {name}')
    #git add name.py / git add * to add all
    #git commit -m "message"
    #git status to check
    #git diff to see the diff

def branch(name):
    print(f'Hi, {name}')
    #git branch to check
    #git branch "name"
    #git checkout "name" to switch to that branch
    #git checkout master , git merge "name" to merge the file to the master

def add_origin(name):
    print(f'Hi, {name}')
    #git remote add origin link
    #git remote -v to check
    #git push --set-upstream origin master
    #git push -u origin

def tag(name):
    print(f'Hi, {name}')
    #git tag -a v1.0 -m "first release"
    #git push origin v1.0 then create a release

def submodule(name):
    print(f'Hi, {name}')
    #git add submodule add link
    #git clone link
    #git log to check history


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
