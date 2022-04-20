CC = gcc
TARGET = class.exe
OBJECT = student.o teacher.o main.o textbook.o
CFLAGS = -g -c

$(TARGET) : $(OBJECT)
	$(CC) -o $(TARGET) $(OBJECT)

clean :
	rm *.o class.exe
