CREATE TEMPORARY TABLE t
(
	message TEXT,
	processing_time TIMESTAMP NOT NULL,
	etl_execution_time DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS processed_logs
(
	inserted_on TIMESTAMP NOT NULL,
	dag_id VARCHAR(255) NOT NULL,
	message TEXT,
	processing_time TIMESTAMP NOT NULL,
	etl_execution_time DATE NOT NULL
);

COPY t(message, processing_time, etl_execution_time) FROM '%(log_dir)s/processed_log.csv' WITH (FORMAT CSV, DELIMITER ';', HEADER true);

INSERT INTO processed_logs(inserted_on, dag_id, message, processing_time, etl_execution_time)
SELECT now() AS inserted_on, {{ dag.dag_id }} AS dag_id, message, processing_time, etl_execution_time
FROM t;