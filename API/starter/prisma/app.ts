import express from "express"
import prisma from "./prisma" // importing the prisma instance we created.
import fetch from "node-fetch";

const app = express()
app.use(express.json())

const PORT = process.env.PORT || 3000

app.listen(PORT, () => console.log(`Server is running on port ${PORT}`))

app.get("/", async (req, res) => {
    return {"Hello": "World"}
})

app.get("/test", async function(req, res) {
    let obj;

    await fetch('http://127.0.0.1:8000/pythontest').then(res => res.json()).then(data => obj = data).catch(err => console.log(err));
    res.json({"Bdd": obj})

})
