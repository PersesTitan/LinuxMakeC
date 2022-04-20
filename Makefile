CC = gcc
TARGET = class.exe
OBJECT = student.o teacher.o main.o textbook.o

$(TARGET) : $(OBJECT)
	$(CC) : $(OBJECT)
		$(CC) -o $(TARGET) $(OBJECT)

student.o : student.c
	gcc -c student.c

teacer.o : teacher.c
	gcc -c teacher.c

main.o : main.c
	gcc -c main.c

textbook.o : textbook.c
	gcc -c textbook.c

clean :
	rm *.o class.exe
