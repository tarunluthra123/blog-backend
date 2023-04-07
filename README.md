# Blog App Backend
Backend server for a blogging application.
Uses Postgres database with Django Rest Framework. For authentication, it uses JWT tokens.
This app has been deployed on render.com at https://blog-backend-bpxd.onrender.com

## Postman Collection
https://www.postman.com/restless-resonance-609196/workspace/my-workspace/collection/16469255-e91288b1-d5a6-4670-98c9-48a5c60b9091?action=share&creator=16469255

## Problem Statement
Make a web application for blogging which has built in capabilities to handle various users.

---

## Requirements
- CRUD capabilities for **USERS**
- CRUD capabilities for **BLOGS** which would be scoped under a **USER**. *i.e. only the user which creates a blog would be able to modify/delete it*
- All **USERS** should be able to view **BLOGS** which have been posted
- A **USER** should be able to write a **BLOG** and post it for everyone to see
- A **USER** should be able to follow another **USER** so that their **BLOGS** have a higher priority on the former **USER**'s feed
- **USERS** should be able to **COMMENT** under a **BLOG**. *These comments would be public*
- **USERS** should be able to LIKE / UNLIKE a **BLOG**

---

## Schema diagram

![](blogging-app.drawio.svg)
