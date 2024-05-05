package edu.uao.project.controller;

import java.util.List;

import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import edu.uao.project.model.TutorCurso;
import edu.uao.project.service.TutorCursoServiceIMPL;
import lombok.RequiredArgsConstructor;

@RestController
@RequestMapping("/api/v5")
@RequiredArgsConstructor
public class TutorCursoControl {
	
	private final TutorCursoServiceIMPL tutorCursoService;
	
	@PostMapping("/TutorsCourses")
	public void save(@RequestBody TutorCurso tutorCurso) {
		tutorCursoService.save(tutorCurso);
	}
	
	@GetMapping("/TutorsCourses")
	public List<TutorCurso> findAll(){
		return tutorCursoService.findAll();
	}
	
	@GetMapping("/TutorsCourses/{id}")
	public TutorCurso findById(@PathVariable String id) {
		return tutorCursoService.findById(id).get();
	}
	@DeleteMapping("/TutorsCourses/{id}")
	public void deleteById(@PathVariable String id) {
		tutorCursoService.deleteById(id);
	}
	@PutMapping("/TutorsCourses")
	public void update(@RequestBody TutorCurso tutorCurso) {
		tutorCursoService.save(tutorCurso);
		
	}
}
