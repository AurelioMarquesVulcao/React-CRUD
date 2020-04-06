const express = require("express");
const mongoose = require("mongoose");
const router = express.Router();
const Place = require("../models/places");

router.get("/", (req, res, next) => {
  Place.find()
    .exec()
    .then(placeList => res.status(200).json(placeList))
    .catch(err => res.status(500).json({ error: err }));
});

router.get("/:placeId", (req, res, next) => {
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

router.post("/", (req, res, next) => {
  const place = new Place({
    // _id: new mongoose.Types.ObjectId(),
    country: req.body.country,
    cases: req.body.cases,
    death: req.body.death,
    date: req.body.date
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

router.delete("/:placeId", (req, res, next) => {
  const id = req.params.placeId;
  Place.remove({ _id: id })
  .exec()
  .then(result => {
    res.status(200).json(result);
  })
  .catch(err => res.status(500).json({ error: err }));
});

module.exports = router;


