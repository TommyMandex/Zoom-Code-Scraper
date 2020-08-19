# Zoom-Code-Scraper
Finds Zoom Codes for you.

## Information
This tool specifically searches for Zoom Codes/URLs posted recently by users on Twitter. It filters possible results.

I got the idea from verdict, he made a similar tool a few months ago but using TweetDeck. Mine uses Twitter's official API.<br/>
His Discord username: verdict#0200

## Preview
![](https://i.imgur.com/8mfXao4.png)<br/>
![](https://i.imgur.com/hRONic6.png)

## Usage
- Python 3.6 or above is required.
- I develop for Windows machines only and do not intentionally support other operating systems.
- If you do not already have the **requests** library installed, run setup.py — make sure PIP is added to PATH.
1. Run main.py.
2. Done.

If it returns "Outdated cookies":
1. Launch any HTTP debugger — built-in browser debuggers work. In this example, I am going to use Chrome's built-in debugger.
2. Head over to the [Network tab](https://i.imgur.com/UAzJL0R.png).
3. Visit [this URL](https://twitter.com/search?q=zoom%20code&src=typed_query&f=live) — in the same tab.
4. Click on [this request](https://i.imgur.com/Pxc4gGh.png) for further details.
5. Under the "Request Headers" tab, copy the [authorization header's value](https://i.imgur.com/38aPHHV.png). Replace the authorization header's value with the new one in main.py.
6. Below the authorization header, copy the [cookie's value](https://i.imgur.com/OphifTK.png). Replace the cookie header's value with the new one in main.py.
7. Again, under the "Request Headers" tab, copy the [x-csrf-token's value](https://i.imgur.com/ri9wClV.png). Replace the x-csrf-token header's value with the new one in main.py.
8. Below the x-csrf-token header, copy the [x-guest-token's value](https://i.imgur.com/Rp3xE5L.png). Replace the x-guest-token header's value with the new one in main.py.
9. Relaunch main.py!

I am aware I could have made a simple loading script for the headers, but I just wanted to get the idea out.
