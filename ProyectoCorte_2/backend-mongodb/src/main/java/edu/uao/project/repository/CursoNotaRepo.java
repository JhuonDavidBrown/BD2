package edu.uao.project.repository;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

import edu.uao.project.model.CursoNota;

@Repository //definirla como repositorio
public interface CursoNotaRepo extends MongoRepository<CursoNota,String>{
	
}	
