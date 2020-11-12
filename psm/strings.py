class strings(object):
    APIID = (
        "Send me your `API_ID` you can find it on my.telegram.org after you logged in."
    )
    APIHASH = "Send me your `API_HASH` you can find it on my.telegram.org after you logged in."
    PHONETOKEN = (
        "Now send me your `phone number` in international format or your `bot_token`"
    )
    ERROR = "**Something went wrong:** ```{err}```"
    FLOODWAIT = (
        "I cannot create session for you.\nYou have a floodwait of: `{e.x} seconds`"
    )
    INVALIDNUMBER = (
        "Phone number is invalid, Make sure you double check before sending."
    )
    APIINVALID = "Your `API_ID` or `API_HASH` given is Invalid. Try again"
    PHONECODE = "send me your code in the format `1-2-3-4-5` and not `12345`"
    PASSWORD = "The entered Telegram Number is protected with 2FA. Please enter your second factor authentication code.\n__This message will only be used for generating your string session, and will never be used for any other purposes than for which it is asked.__"
    PHONECODEINVALID = "The code you sent seems Invalid, Try again."
    PHONECODE_EXPIRED = "The Code you sent seems Expired. Try again."
    DONEPHONE = ("All Done! Check your Saved Messages for your Session String.",)
    BOTTOKENINVALID = (
        "BotToken Invalid: make sure you are sending a valid BotToken from @BotFather"
    )
