package edu.uao.project.service;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import edu.uao.project.model.Tutor;
import edu.uao.project.repository.TutorRepo;
import lombok.RequiredArgsConstructor;

@Service
@RequiredArgsConstructor
public class TutorServiceIMPL {
    
    private final TutorRepo tutorRepo;
    
    public void save (Tutor tutor) {
    	tutorRepo.save(tutor);
    }
    
    public List<Tutor> findAll(){
    	return tutorRepo.findAll();
    }
    
    public Optional<Tutor>findById(String id) {
    	return tutorRepo.findById(id);
    }
    
    public void deleteById(String id) {
    	tutorRepo.deleteById(id);
    }
    

}