package edu.uao.project.repository;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

import edu.uao.project.model.Tutor;

@Repository
public interface TutorRepo extends MongoRepository<Tutor,String> {

}
