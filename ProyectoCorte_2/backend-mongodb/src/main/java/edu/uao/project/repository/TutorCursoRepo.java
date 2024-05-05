package edu.uao.project.repository;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

import edu.uao.project.model.TutorCurso;

@Repository //definirla como repositorio
public interface TutorCursoRepo extends MongoRepository<TutorCurso,String>{
	
}	
