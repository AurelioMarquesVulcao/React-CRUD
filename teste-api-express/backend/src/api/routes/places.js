const express = require("express");
const mongoose = require("mongoose");
const router = express.Router();
const Place = require("../models/places");


// Pega todos os indices do banco de dados
router.get("/", (req, res, next) => {
  Place.find()
    .exec()
    .then(placeList => res.status(200).json(placeList))
    .catch(err => res.status(500).json({ error: err }));
});

// Exibe um indice pelo id.
router.get("/:userId", (req, res, next) => {
  const id = req.params.placeId;
  Place.findById(id)
    .exec()
    .then(place => {
      if (place) {
        res.status(200).json(place);
      } else {
        res.status(404).json({ message: "Local Não encontrado" });
      }
    })
    .catch(err => {
      res.status(500).json({ error: err });
    });
});

// Grava apenas um dado no banco de dados
router.post("/", (req, res, next) => {
  const place = new Place({
    // _id: new mongoose.Types.ObjectId(),
    // country: req.body.country,
    name: req.body.name,
    email: req.body.email,
    // quantity: req.body.quantity
  });
  place
    .save()
    .then(result => console.log(result))
  // está retornando erro mesmo com status 200
  //.cath(err => console.log(err));
  res.status(200).json({
    message: "New place created"
  });
});

// Deleta apenas um dado no banco de dados
router.delete("/:userId", (req, res, next) => {
  const id = req.params.placeId;
  Place.remove({ _id: id })
  .exec()
  .then(result => {
    res.status(200).json(result);
  })
  .catch(err => res.status(500).json({ error: err }));
});

// vai atualizar um registro
router.patch("/:userId", (req, res, next) => {
  const id = req.params.placeId
  Place.updateOne({
    _id: id,
    // country: req.body.country,
    name: req.body.name,
    email: req.body.email,
    // quantity: req.body.quantity
  })
  .exec()
  .then(result => console.log(result))
  .catch(err => res.status(500).json({ error: err }));
  res.status(200).json({
    message: "Successfully edited"
  });
});


// trabalhando nessa função

// router.put("/:placeId", (req, res, next) => {
//   const id = req.params.placeId
//   Place.findOneAndUpdate({
//     _id: id,
//     country: req.body.country,
//     cases: req.body.cases,
//     death: req.body.death,
//     date: req.body.date,
    
//   },{new: true})
//   .exec()
//   .then(result => console.log(result))
//   .catch(err => res.status(500).json({ error: err }));
//   res.status(200).json({
//     message: "Successfully edited"
//   });
// });


module.exports = router;
