First of all, we must import the kivy library in our code, that is the first step

The "app" class is in charge of inheriting a set of parameters and methods that are the heart of the application, that is, what allows you to build based on this and the work of the kivy library.

The "run ()" method belongs to this class, and is in charge of generating an instance of the application.

The "build ()" method is in charge of providing the information of the application's content to the "heart", this is predetermined to generate an empty window, but you overwrite the function (as we did) you can add the content you want.

The code:
  if __name__ == "__main__":
  
It does a check if the code we are executing is primary or is being inherited as secondary code towards a main code.

After that we import the widget module from the uix package that represents the user experience. A Widget is the main base of the content of our application, almost everything inherits from this class.
