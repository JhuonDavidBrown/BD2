package edu.uao.project.service;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import edu.uao.project.model.TutorCurso;
import edu.uao.project.repository.TutorCursoRepo;
import lombok.RequiredArgsConstructor;

@Service
@RequiredArgsConstructor
public class TutorCursoServiceIMPL {
    
    private final TutorCursoRepo tutorCursoRepo;
    
    public void save (TutorCurso tutorCurso) {
    	tutorCursoRepo.save(tutorCurso);
    }
    
    public List<TutorCurso> findAll(){
    	return tutorCursoRepo.findAll();
    }
    
    public Optional<TutorCurso>findById(String id) {
    	return tutorCursoRepo.findById(id);
    }
    
    public void deleteById(String id) {
    	tutorCursoRepo.deleteById(id);
    }
    

}