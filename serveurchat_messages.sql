-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: serveurchat
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `messages` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user` varchar(255) DEFAULT NULL,
  `message` text,
  `timestamp` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=130 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (1,'yann','hey','2023-12-17 15:38:39'),(2,'yann','ça va?','2023-12-17 15:38:51'),(3,'thibaut','yo je viens d\'arriver','2023-12-17 15:39:26'),(4,'yann','hey','2023-12-19 19:20:16'),(5,'inscription  yann','inscription  inscription','2023-12-19 19:34:43'),(6,'inscription  yann','yann','2023-12-19 19:35:29'),(7,'inscription ','inscription ','2023-12-19 19:46:32'),(8,'inscription ','inscription ','2023-12-19 19:46:33'),(9,'inscription ','inscription ','2023-12-19 19:46:33'),(10,'inscription ','inscription ','2023-12-19 19:46:33'),(11,'inscription ','inscription ','2023-12-19 19:46:35'),(12,'inscription ','inscription yann','2023-12-19 19:46:39'),(13,'inscription ','yann','2023-12-19 19:46:52'),(14,'inscription yann','inscription yann','2023-12-19 19:51:52'),(15,'inscription yann','hey','2023-12-19 19:51:58'),(16,'yann','hey','2023-12-20 17:40:44'),(17,'yann','comment ça va','2023-12-20 17:40:50'),(18,'yann','hey','2023-12-20 17:48:55'),(19,'yann','ça a mis longtemp','2023-12-20 17:49:13'),(20,'titi','hz','2023-12-20 19:02:06'),(21,'titi','he','2023-12-20 19:02:07'),(22,'yann','hay','2023-12-21 17:29:40'),(23,'test3','test3: fefe','2023-12-21 19:27:39'),(24,'test3','hey','2023-12-21 19:51:52'),(25,'test3','comment tu vas?','2023-12-21 19:52:06'),(26,'inscription test8','test8','2023-12-21 20:01:31'),(27,'inscription test8','hey','2023-12-21 20:01:34'),(28,'inscription test8','yo','2023-12-21 20:02:07'),(29,'yann','hey','2023-12-21 20:03:05'),(30,'inscription test8','yo','2023-12-21 20:03:16'),(31,'test47','fefeffez','2023-12-23 09:42:21'),(32,'test47','fezefz','2023-12-23 09:42:22'),(33,'test47','fezfe','2023-12-23 09:42:23'),(34,'dada','dada','2023-12-23 09:44:08'),(35,'connexion yann','dadada','2023-12-23 09:55:01'),(36,'connexion yann','dada','2023-12-23 09:55:02'),(37,'connexion yann','da','2023-12-23 09:55:03'),(38,'connexion yann','da','2023-12-23 09:55:04'),(39,'connexion yann','dada','2023-12-23 09:55:05'),(40,'connexion yann','dada','2023-12-23 09:55:07'),(41,'connexion yann','dada','2023-12-23 09:55:09'),(42,'connexion yann','fefaefeaf','2023-12-23 09:59:53'),(43,'connexion yann','feafea','2023-12-23 09:59:54'),(44,'connexion yann','fezfez','2023-12-23 09:59:56'),(45,'connexion yann','fezfz','2023-12-23 09:59:57'),(46,'connexion yann','fezf','2023-12-23 09:59:57'),(47,'yann','hey','2023-12-23 13:20:14'),(48,'yann','salut','2023-12-23 13:21:35'),(49,'yann','hey','2023-12-23 13:24:49'),(50,'yann','hey','2023-12-23 13:25:25'),(51,'yann','hey','2023-12-23 13:32:51'),(52,'yann','hey','2023-12-23 13:37:51'),(53,'yann','comment tu vas','2023-12-23 13:38:00'),(54,'yann','re','2023-12-23 13:39:25'),(55,'yann','hey','2023-12-23 13:56:11'),(56,'yann','re','2023-12-23 13:56:14'),(57,'yann','re','2023-12-23 13:56:42'),(58,'yann','hey','2023-12-23 14:08:57'),(59,'yann','hey','2023-12-23 14:09:32'),(60,'yann','hay','2023-12-23 14:09:50'),(61,'yann','hay','2023-12-23 14:13:15'),(62,'yann','hey','2023-12-23 14:13:56'),(63,'mathieu','yo','2023-12-23 14:14:01'),(64,'mathieu','comment tu vas?','2023-12-23 14:14:07'),(65,'yann','hey','2023-12-23 14:14:28'),(66,'mathieu','yo je m\'appelle mathieu','2023-12-23 14:15:30'),(67,'yann','salut mathieu','2023-12-23 14:15:35'),(68,'yann','salut','2023-12-23 14:16:03'),(69,'test47','hey','2023-12-23 14:18:16'),(70,'yann','hey','2023-12-23 14:43:46'),(71,'yann','yo','2023-12-23 14:43:49'),(72,'yann','yo','2023-12-23 14:47:47'),(73,'yann','yo','2023-12-23 14:49:51'),(74,'yann','hey','2023-12-23 14:56:40'),(75,'yann','yo','2023-12-23 14:56:54'),(76,'yann','/join General','2023-12-23 17:27:12'),(77,'yann','salut','2023-12-23 17:27:23'),(78,'mathieu','yo','2023-12-23 17:27:50'),(79,'yann','/join General','2023-12-24 08:37:27'),(80,'yann','/join General','2023-12-24 08:37:32'),(81,'yann','/join General','2023-12-24 08:37:34'),(82,'yann','/join General','2023-12-24 08:38:10'),(83,'yann','/join General','2023-12-24 08:38:12'),(84,'yann','/join General','2023-12-24 08:38:13'),(85,'yann','/join General','2023-12-24 08:39:03'),(86,'yann','/join General','2023-12-24 08:39:05'),(87,'yann','/join General','2023-12-24 08:39:06'),(88,'yann','/join General','2023-12-24 08:49:44'),(89,'yann','/join General','2023-12-24 08:49:45'),(90,'yann','/join General','2023-12-24 08:49:46'),(91,'yann','/join General','2023-12-24 08:49:47'),(92,'yann','/join General','2023-12-24 08:50:18'),(93,'yann','/join General','2023-12-24 08:51:18'),(94,'yann','/join General','2023-12-24 08:52:26'),(95,'yann','/join General','2023-12-24 08:52:58'),(96,'yann','/join General','2023-12-24 08:53:15'),(97,'yann','/join Blabla','2023-12-24 13:22:39'),(98,'yann','/join Comptabilite','2023-12-24 13:22:41'),(99,'yann','/join Marketing','2023-12-24 13:22:42'),(100,'yann','/join Comptabilite','2023-12-24 13:22:45'),(101,'yann','/join Blabla','2023-12-24 13:22:45'),(102,'yann','/join General','2023-12-24 13:22:46'),(103,'yann','/join Informatique','2023-12-24 13:24:25'),(104,'mathieu','hey','2023-12-24 13:24:30'),(105,'yann','hey','2023-12-24 13:24:34'),(106,'yann','hey','2023-12-24 13:48:05'),(107,'yann','/join Blabla','2023-12-24 13:48:09'),(108,'yann','/join Informatique','2023-12-24 13:48:12'),(109,'yann','/join Blabla','2023-12-24 13:48:13'),(110,'mathieu','hey','2023-12-24 13:48:27'),(111,'yann','hey','2023-12-24 13:48:31'),(112,'yann','/join Comptabilite','2023-12-24 13:48:36'),(113,'yann','hey','2023-12-24 13:48:39'),(114,'yann','/join Comptabilite','2023-12-24 13:57:04'),(115,'mathieu','hey','2023-12-24 13:57:31'),(116,'yann','hey','2023-12-24 13:57:35'),(117,'yann','hey','2023-12-25 14:16:40'),(118,'yann','hello','2023-12-25 14:16:54'),(119,'yann','hey','2023-12-25 14:33:59'),(120,'yann','hey','2023-12-25 15:40:30'),(121,'yann','fafezaf','2023-12-25 15:40:43'),(122,'yann','hey','2023-12-25 16:05:03'),(123,'yann','hey','2023-12-26 15:49:24'),(124,'Sarah','hey','2023-12-28 17:50:22'),(125,'yann','hey','2023-12-29 17:15:24'),(126,'yann','test1','2023-12-29 17:39:40'),(127,'test10','salut yann','2023-12-29 17:40:32'),(128,'yann','Bonjour','2023-12-29 19:59:32'),(129,'mathieu','Bonjour yann','2023-12-29 20:00:06');
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-30 16:09:41
