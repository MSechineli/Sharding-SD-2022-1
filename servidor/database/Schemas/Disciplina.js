import mongoose from "mongoose"

const DisciplinaSchema = mongoose.Schema({
  codigo: {
    type: String,
    require: true
  },
  nome: {
    type: String,
    require: true
  },
  professor: {
    type: String,
    require: true
  },
  cod_curso: {
    type: Number,
    require: true
  }
})

export default DisciplinaSchema