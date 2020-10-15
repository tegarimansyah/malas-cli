# malas-cli
A collection of automating boring stuff for devops in single command line.

Dependency:

* click
* PyInquirer
* cookiecutter

# Example Command

For now, the script will only run on Ubuntu and derivative

## Malas Install

```bash
$ malas install docker # will install docker, docker compose and set to current user
$ malas install nginx # will instal 
```

## Malas Set Up

```bash
$ malas setup nginx # Generate config and apply it
$ malas setup cloudflare # Create new dns record for your cloudflare
$ malas setup wireguard # Create new user for your wireguard config
$ malas setup ssh # Create ssh keygen then transfer to server or copy to clipboard
$ malas setup kubernetes # Create deployment or config
```

## Malas Build 

```bash
$ malas build docker # Connect to docker (or remote server), build, tagging and push to registry
```

## Malas Deploy

```bash
$ malas deploy docker-compose # Run green-blue docker compose
$ malas deploy django # Pull from github, migrate, collectstatic then restart systemd
```

If you are really lazy to remind everything (IP, domain, etc), just centralize it. 

## Malas Login

```bash
$ malas register
$ malas login
```