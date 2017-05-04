from neural_nets.simple_rnn.simple_rnn_trainer import simple_rnn_trainer

if __name__ == "__main__":
    print("Imported libs.")
    trainer = simple_rnn_trainer()
    trainer.prepare_datasets()
    trainer.define_hyperparameters()
    trainer.define_variables()
    trainer.define_graph()
    trainer.print_trainer_details()
    trainer.begin_training()

