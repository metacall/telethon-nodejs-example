# telethon-nodejs
Using Telethon (Python) from NodeJS with MetaCall.

TODO

...

## Install

Install MetaCall CLI:

```sh
curl -sL https://raw.githubusercontent.com/metacall/install/master/install.sh | sh
```

Install application dependencies:

```sh
metacall pip3 install -r requirements.txt
metacall npm install metacall
```

## Run the Application

```sh
metacall index.js
```

For testing it, ...


## Docker Compose

An alternative version with Docker Compose is provided. For setting it up, first of all it is needed to set up **`.env.template`**:

 1) Copy the file and rename it into **`.env`**.

    ```sh
    mv .env.template .env
    ```

 2) Fill the environment variables with your Telegram API ID, Hash and the name for your session. You can see how to obtain the keys from Telegram official documentation: https://core.telegram.org/api/obtaining_api_id.

    ```sh
    nano .env
    ```

 3) Then you will be able to build and run MetaCall with Docker Compose:

    ```sh
    docker-compose build
    docker-compose up
    ```
