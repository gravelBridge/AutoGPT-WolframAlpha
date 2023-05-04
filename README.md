# AutoGPT-WolframAlpha Plugin 🔢

An AutoGPT plugin to enable communication with WolframAlpha for solving math problems and getting information.

![Screenshot 2023-05-03 at 7 45 54 PM](https://user-images.githubusercontent.com/107640947/236104175-2cfd9344-64e6-4647-8343-72d69b1bc0d0.png)

## 📚 Requirements

1. **Python Package**: Install the WolframAlpha Python package:

`pip install wolframalpha`

2. **WolframAlpha API Key**: Obtain a WolframAlpha API key by signing up for a free account at the [WolframAlpha Developer Portal](https://developer.wolframalpha.com/portal/signup.html) and creating an app. After creating the app, you will receive an `APP_ID`.

## 🔧 Configuration

1. **Update the .env file**: Add the following lines to your `.env` file:

```
################################################################################
### WOLFRAM ALPHA PLUGIN SETTINGS
################################################################################

WOLFRAM_ALPHA_APP_ID = your_app_id
```

2. **Allowlist Plugin**: In your `.env` file, search for `ALLOWLISTED_PLUGINS` and add this plugin:

```
################################################################################

ALLOWLISTED PLUGINS
################################################################################

#ALLOWLISTED_PLUGINS - Sets the listed plugins that are allowed (Example: plugin1,plugin2,plugin3)
ALLOWLISTED_PLUGINS=AutoGPTWolframAlpha
```


## 🚀 Usage

After installing the package and configuring the settings, you can use the AutoGPT-WolframAlpha plugin to allow AutoGPT to solve math problems and obtain information from WolframAlpha.

Example:

1. **Configure Auto-GPT**: Set up Auto-GPT with the following parameters:
- Name: `MathSolverGPT`
- Role: `an ai designed to follow user instructions`
- Goals:
  1. Goal 1: `Solve the integral of x^2 from 0 to 3`
  2. Goal 2: `Terminate`

2. **Run Auto-GPT**: Launch Auto-GPT, which should use the WolframAlpha plugin to solve the math problem and return the result.


