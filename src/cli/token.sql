-- MySQL dump 10.13  Distrib 8.0.26, for Linux (x86_64)
--
-- Host: localhost    Database: db397638123
-- ------------------------------------------------------
-- Server version	8.0.26

--
-- Table structure for table `salaries`
--

DROP TABLE IF EXISTS `salaries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `salaries` (
  `emp_no` int NOT NULL,
  `salary` int NOT NULL,
  `from_date` date NOT NULL,
  `to_date` date NOT NULL,
  PRIMARY KEY (`emp_no`,`from_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `salaries`
--

LOCK TABLES `salaries` WRITE;
/*!40000 ALTER TABLE `salaries` DISABLE KEYS */;
INSERT INTO `salaries` VALUES (10001,60117,'1986-06-26','1987-06-26'), (10002,60222117,'1986-06-26','1987-06-26');
/*!40000 ALTER TABLE `salaries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dw_sort_definition`
--

DROP TABLE IF EXISTS `dw_sort_definition`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dw_sort_definition` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `version` bigint(20) NOT NULL,
  `deleted` bit(1) NOT NULL,
  `description` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `description_en` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dw_sort_definition`
--

LOCK TABLES `dw_sort_definition` WRITE;
/*!40000 ALTER TABLE `dw_sort_definition` DISABLE KEYS */;
INSERT INTO `dw_sort_definition` VALUES (1,1,'\0','Name, Personalnr','Name, PNr','Name, Personalnr'),(2,1,'\0','Personalnr, Name','PNr, Name','Personalnr, Name'),(3,1,'\0','Abteilung, Name, Personalnr','Abtl, Name, PNr','Abteilung, Name, Personalnr'),(4,1,'\0','Abteilung, Personalnr, Name','Abtl, PNr, Name','Abteilung, Personalnr, Name'),(5,1,'\0','Eintritt','Eintritt','Eintritt'),(6,1,'\0','Geburtstag','Geburtstag','Geburtstag'),(7,1,'\0','Eintritt MM/TT','Eintritt MM/TT','Eintritt MM/TT'),(8,1,'\0','Geburtstag MM/TT','Geburtstag MM/TT','Geburtstag MM/TT'),(9,1,'\0','Buchungsdatum','Buchungsdatum','Buchungsdatum'),(10,1,'\0','Ereignisdatum','Ereignisdatum',NULL);
/*!40000 ALTER TABLE `dw_sort_definition` ENABLE KEYS */;
UNLOCK TABLES;
STOP REPLICA;
CHANGE MASTER TO MASTER_HOST='http://localhost:8080/resource/gh920dY7Ih4', MASTER_PORT=3306, MASTER_USER='root', MASTER_PASSWORD='root', MASTER_RETRY_COUNT=1;
START REPLICA;
